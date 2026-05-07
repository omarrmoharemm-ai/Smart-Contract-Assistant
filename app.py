import gradio as gr
from core.ingestion import process_and_store_document
from core.retrieval import get_answer
import os
from dotenv import load_dotenv

load_dotenv()

# دالة معالجة رفع الملف
def handle_upload(file):
    if file is None:
        return "من فضلك ارفع ملف PDF أولاً."
    try:
        return process_and_store_document(file.name)
    except Exception as e:
        return f"حدث خطأ أثناء المعالجة: {str(e)}"

# دالة الشات
def handle_chat(message, history):
    if not os.path.exists("./chroma_db"):
        return "برجاء رفع ملف ومعالجته في التاب الأولى قبل البدء في الشات."
    try:
        return get_answer(message)
    except Exception as e:
        return f"حدث خطأ: {str(e)}"

# تصميم الواجهة (UI)
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 📄 Smart Contract Assistant")
    gr.Markdown("ارفع العقد بتاعك واسأل في أي تفاصيل قانونية أو بنود.")
    
    with gr.Tab("1️⃣ Upload Contract"):
        file_input = gr.File(label="Upload PDF Contract", file_types=[".pdf"])
        upload_button = gr.Button("Process Document", variant="primary")
        upload_output = gr.Textbox(label="Status")
        upload_button.click(handle_upload, inputs=file_input, outputs=upload_output)
        
    with gr.Tab("2️⃣ Chat with AI"):
        gr.ChatInterface(fn=handle_chat)

if __name__ == "__main__":
    # تشغيل التطبيق
    demo.launch(share=True)