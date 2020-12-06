def escape_html(text: str) -> str:
    return text.replace("&", "&amp").replace("<", "&lt").replace(">", "&gt")
