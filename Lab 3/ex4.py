def build_xml_element(tag, content, **kwargs):
    # Inițializez elementul XML ca șir cu eticheta de deschidere
    xml_element = f"<{tag}"

    # Adaug orice atribute cheie-valoare la elementul XML
    for key, value in kwargs.items():
        xml_element += f' {key}="{value}"'

    # Adaug conținutul și închid eticheta
    xml_element += f'>{content}</{tag}>'

    return xml_element

result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(result)  # <a href="http://python.org" _class="my-link" id="someid">Hello there</a>'
