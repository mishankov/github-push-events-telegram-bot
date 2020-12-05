def escape_html(text: str) -> str:
    return text.replace("<", "&lt").replace(">", "&gt").replace("&", "&amp")
