import hashlib
import json


def find_nonce(input_json, difficulty):
    """Given a JSON string, find a nonce that will cause the SHA256 hash of the block
    to begin with 'difficult' zero bits. """
    for i in range(0, 1000000):
        input_json['block']['nonce'] = i
        input_json['block']['data'] = sorted(input_json['block']['data'])
        sha_digest = get_sha_digest(input_json)
        if int(sha_digest[0:difficulty]) == 0:
            return i

    print("not found")
    return None


def get_sha_digest(json_obj):
    sha = hashlib.sha256(json.dumps(json_obj['block'], sort_keys=True).replace(' ', '').encode())
    hex = sha.hexdigest()
    b_arr = []
    for ch in hex:
        if '0' <= ch <= '9':
            number = int(ch)
        else:
            number = 10 + (ord(ch) - ord('a'))
        b_arr.append(format(number, '0>4b'))
    return ''.join(b_arr)
