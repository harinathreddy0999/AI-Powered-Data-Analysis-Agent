import os
import subprocess
import sys

def main():
    """
    Run the Streamlit application.
    """
    print("Starting AI Data Analysis Agent...")
    
    # Check for .env file
    if not os.path.exists(".env"):
        print("\nWARNING: No .env file found.")
        create_env = input("Would you like to create a .env file now? (y/n): ")
        
        if create_env.lower() == 'y':
            api_key = input("Enter your OpenAI API key: ")
            
            with open(".env", "w") as f:
                f.write(f"OPENAI_API_KEY={api_key}\n")
                f.write("OPENAI_MODEL=gpt-4o\n")
                f.write("MAX_FILE_SIZE_MB=100\n")
            
            print("Created .env file with your API key.")
        else:
            print("\nNote: You will need to provide your OpenAI API key in the application.")
    
    # Run the Streamlit app
    streamlit_cmd = [sys.executable, "-m", "streamlit", "run", "src/app.py"]
    
    try:
        subprocess.run(streamlit_cmd)
    except KeyboardInterrupt:
        print("\nStopping application...")
    except Exception as e:
        print(f"\nError running application: {str(e)}")
        print("\nTry running the application directly with:")
        print("  streamlit run src/app.py")

if __name__ == "__main__":
    main() 