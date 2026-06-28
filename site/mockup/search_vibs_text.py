import os

app_path = r"C:\Users\larse\Documents\Interne prosjekter\Vibs\vibs-boligpass\src\App.jsx"

def search():
    if not os.path.exists(app_path):
        print(f"File not found: {app_path}")
        return
        
    try:
        with open(app_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if "vibs" in line.lower():
                print(f"Line {i}: {line.strip()[:140]}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    search()
