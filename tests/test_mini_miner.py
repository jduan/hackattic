from hackattic.mini_miner import (find_nonce, get_sha_digest)


def test_get_sha_digest():
    # input_json = """
    # {"difficulty": 13, "block": {"nonce": null, "data": [["5c1bb1f4f3b45aa05af0780e829da5e7", 83], ["373496c09b79effa2fc87565c0f74ea0", -75], ["f5dd36437e76e879edf7668134486976", -37], ["1e721115525148eb08349c9484af1830", 73]]}}
    # """
    input_json = {
            "difficulty": 13,
            "block": {
                "data": [],
                "nonce": 45
            }
        }
    sha_digest = get_sha_digest(input_json)
    print(f"sha_digest: {sha_digest}")


def test_find_nonce():
    input_json = {
        "difficulty": 13,
        "block": {
            "nonce": None,
            "data": [
                [
                    "35beb6c496977bb83c48eeb2a28dffee",
                    9
                ],
                [
                    "ab7ca9c67a5b67e70b3ea4f387b0604a",
                    -1
                ],
                [
                    "2fb30a9f460faecdc07ff59c72fb8ed1",
                    83
                ]
            ]
        }
    }

    nonce = find_nonce(input_json, input_json['difficulty'])
    assert nonce == 9026
