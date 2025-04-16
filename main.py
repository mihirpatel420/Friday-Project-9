import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Debug print for API key
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("Warning: No API key found in environment variables")
elif api_key == "your_api_key_here":
    print("Warning: API key is still set to default placeholder value")
else:
    print("API key loaded (first 4 characters):", api_key[:4])

class TextCompletionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Completion App")
        self.root.geometry("800x600")
        
        # Initialize OpenAI client
        try:
            self.client = OpenAI(api_key=api_key.strip())  # Strip any whitespace from the key
            # Test the API key with a simple request
            available_models = self.client.models.list()
            print("Available models:", [model.id for model in available_models.data])
        except Exception as e:
            error_msg = f"API Error: {str(e)}\n\n"
            error_msg += "Please check:\n"
            error_msg += "1. Your API key is correct and has no extra spaces\n"
            error_msg += "2. Your OpenAI account has sufficient credits\n"
            error_msg += "3. Your API key hasn't expired\n"
            error_msg += "4. You have access to the GPT models"
            messagebox.showerror("API Error", error_msg)
            root.destroy()
            return
        
        self.setup_ui()
        
    def setup_ui(self):
        # Model selection
        model_frame = tk.Frame(self.root)
        model_frame.pack(pady=5, padx=10, fill=tk.X)
        
        tk.Label(model_frame, text="Select Model:").pack(side=tk.LEFT)
        self.model_var = tk.StringVar(value="gpt-3.5-turbo-0125")
        model_options = [
            "gpt-3.5-turbo-0125",
            "gpt-3.5-turbo-1106",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-16k",
            "gpt-3.5-turbo-instruct"  # Added another model option
        ]
        model_dropdown = ttk.Combobox(model_frame, textvariable=self.model_var, values=model_options, state="readonly")
        model_dropdown.pack(side=tk.LEFT, padx=5)
        
        # Input section
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10, padx=10, fill=tk.X)
        
        tk.Label(input_frame, text="Enter your prompt:").pack(anchor=tk.W)
        self.input_text = scrolledtext.ScrolledText(input_frame, height=5)
        self.input_text.pack(fill=tk.X, pady=5)
        
        # Submit button
        self.submit_button = tk.Button(input_frame, text="Submit", command=self.get_completion)
        self.submit_button.pack(pady=5)
        
        # Output section
        output_frame = tk.Frame(self.root)
        output_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        tk.Label(output_frame, text="Completion Result:").pack(anchor=tk.W)
        self.output_text = scrolledtext.ScrolledText(output_frame, height=15)
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
    def get_completion(self):
        prompt = self.input_text.get("1.0", tk.END).strip()
        if not prompt:
            return
            
        try:
            selected_model = self.model_var.get()
            print(f"Attempting to use model: {selected_model}")
            response = self.client.chat.completions.create(
                model=selected_model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            completion = response.choices[0].message.content
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", completion)
            
        except Exception as e:
            error_msg = f"Error with model {self.model_var.get()}: {str(e)}\n\n"
            error_msg += "Please try:\n"
            error_msg += "1. Selecting a different model from the dropdown\n"
            error_msg += "2. Checking your API key permissions\n"
            error_msg += "3. Verifying your account has access to the selected model\n"
            error_msg += "4. Making sure your API key has no extra spaces"
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", error_msg)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextCompletionApp(root)
    root.mainloop() 