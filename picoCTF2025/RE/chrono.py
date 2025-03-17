import random
import time
import socket

def get_random(length, time_offset=0):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(int((time.time() + time_offset) * 1000))  # Adjust the seed with an offset
    s = ""
    for i in range(length):
        s += random.choice(alphabet)
    return s

def main():
    # Connect to the server
    host = "verbal-sleep.picoctf.net"
    port = 56345

    # Try multiple times with adjusted timestamps
    for attempt in range(10):  # Retry the entire process 10 times
        print(f"Attempt {attempt + 1}...")
        for offset in range(-100, 101, 10):  # Try offsets from -100 to +100 milliseconds in steps of 10
            # Predict the token with the current offset
            token_length = 20
            predicted_token = get_random(token_length, time_offset=offset / 1000)  # Convert offset to seconds
            
            print(f"Trying token with offset {offset} ms: {predicted_token}")

            try:
                # Create a socket object
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                # Connect to the server
                sock.connect((host, port))
                
                # Receive the initial welcome message (optional, depending on server behavior)
                welcome_message = sock.recv(1024).decode('utf-8')
                print(welcome_message)
                
                # Send the predicted token to the server
                sock.send(predicted_token.encode('utf-8') + b'\n')
                
                # Receive the server's response
                response = sock.recv(1024).decode('utf-8')
                print(response)
                
                # Check if the response contains the flag or indicates success
                if "Congratulations" in response or "flag" in response:
                    print("Flag found! Exiting...")
                    sock.close()
                    return
                
                # Close the socket
                sock.close()
                
            except Exception as e:
                print(f"An error occurred: {e}")

    print("Failed to find the correct token after multiple attempts.")

if __name__ == "__main__":
    main()