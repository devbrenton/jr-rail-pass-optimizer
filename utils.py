def fare_stoi(s):
    transformed = s[5:s.find("円")]
    if transformed.find(",") != -1:
        transformed = transformed[0:transformed.find(",")]+transformed[transformed.find(",")+1:]
    return int(transformed)