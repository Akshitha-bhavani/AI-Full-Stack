import ollama 
response = ollama.chat(
   model="llama3.2:3b",
   messages=[
       {
           "role":"user",
           "content":"what is ai"
       },
       {
           "role":"system",
           "content":"you are a technical assistant. give structured, precise, and practical answers"
       }
   ] 
)
print(response["message"]["content"])
