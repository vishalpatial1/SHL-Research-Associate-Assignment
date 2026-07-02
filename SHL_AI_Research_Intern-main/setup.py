"""
Setup script to initialize the project
"""

import os
import subprocess
import sys

def create_directories():
    """Create necessary directories"""
    directories = ['data', 'frontend']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

def create_env_file():
    """Create .env file from example if it doesn't exist"""
    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            with open('.env.example', 'r') as f:
                content = f.read()
            with open('.env', 'w') as f:
                f.write(content)
            print("Created .env file from .env.example")
            print("Please update .env with your API keys!")
        else:
            print("Warning: .env.example not found")

def install_dependencies():
    """Install Python dependencies"""
    print("\nInstalling dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return False
    return True

def create_sample_data():
    """Create sample assessment data"""
    print("\nCreating sample assessment data...")
    try:
        from create_sample_data import save_assessments
        save_assessments()
        print("Sample data created!")
    except Exception as e:
        print(f"Error creating sample data: {e}")

def main():
    """Main setup function"""
    print("Setting up SHL Assessment Recommendation System...")
    print("=" * 50)
    
    # Create directories
    create_directories()
    
    # Create .env file
    create_env_file()
    
    # Install dependencies
    if install_dependencies():
        # Create sample data
        create_sample_data()
        
        print("\n" + "=" * 50)
        print("Setup complete!")
        print("\nNext steps:")
        print("1. Update .env file with your GEMINI_API_KEY")
        print("2. Run 'python main.py' to start the API server")
        print("3. Open frontend/index.html in your browser")
    else:
        print("\nSetup incomplete. Please install dependencies manually.")

if __name__ == '__main__':
    main()

