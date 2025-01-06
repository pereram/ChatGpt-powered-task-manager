#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:57:05 2025

@author: meeghageperera
"""

import tkinter as tk
from tkinter import ttk
import openai
import os

# Set your OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

#openai.api_key ="A"

# Function to get ChatGPT response
def chatgpt_response(task, query):
    try:
        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the latest ChatGPT model
            messages=[
                {"role": "system", "content": f"You are an assistant helping with the task: {task}."},
                {"role": "user", "content": query}
            ],
            max_tokens=150,  # Limit the response length
            temperature=0.7  # Adjust the response randomness
        )
        # Extract the reply text
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Function to handle search queries
def handle_search(task, entry, output_label):
    query = entry.get()
    response = chatgpt_response(task, query)
    output_label.config(text=response)

# Main GUI Application
def main_app():
    root = tk.Tk()
    root.title("Task Manager with ChatGPT Assistance")
    root.geometry("600x600")

    # Title Label
    title_label = tk.Label(root, text="Programming Task Manager", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    # Task List Frame
    task_frame = ttk.Frame(root)
    task_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Task List
    tasks = [
        "Learn Python Basics",
        "Build a Calculator",
        "Create a To-Do List",
    ]

    # Output Label for ChatGPT Responses
    output_label = tk.Label(root, text="", wraplength=500, font=("Arial", 10), justify="left")
    output_label.pack(pady=20)

    for task in tasks:
        # Task Frame
        task_item_frame = ttk.Frame(task_frame)
        task_item_frame.pack(fill="x", pady=5)

        # Task Label
        task_label = tk.Label(task_item_frame, text=task, font=("Arial", 12, "bold"))
        task_label.pack(side="left", padx=10)

        # Search Bar
        search_entry = ttk.Entry(task_item_frame)
        search_entry.pack(side="left", padx=10, fill="x", expand=True)

        # ChatGPT Button
        chat_button = ttk.Button(task_item_frame, text="Ask ChatGPT", 
                                  command=lambda t=task, e=search_entry: handle_search(t, e, output_label))
        chat_button.pack(side="left", padx=10)

    # Run the Application
    root.mainloop()

if __name__ == "__main__":
    main_app()
