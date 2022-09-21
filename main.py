import subprocess

if __name__ == "__main__":
    cmd = "streamlit run test.py"
    subprocess.run(cmd, shell=True)
