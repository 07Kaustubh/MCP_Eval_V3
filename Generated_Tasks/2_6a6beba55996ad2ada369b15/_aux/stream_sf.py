import json, sys, resource

def stream_rows(path):
    """Yield parsed row_data dicts from a [{source,row_data}] array without loading the file."""
    dec = json.JSONDecoder()
    buf = ""
    started = False
    with open(path, "r", encoding="utf-8") as f:
        while True:
            chunk = f.read(1 << 20)
            if not chunk and not buf.strip():
                break
            buf += chunk
            if not started:
                i = buf.find("[")
                if i < 0:
                    continue
                buf = buf[i+1:]
                started = True
            while True:
                s = buf.lstrip()
                trimmed = len(buf) - len(s)
                if not s:
                    buf = ""
                    break
                if s[0] in ",":
                    buf = s[1:]
                    continue
                if s[0] == "]":
                    return
                try:
                    obj, end = dec.raw_decode(s)
                except ValueError:
                    buf = buf[trimmed:]
                    break
                buf = s[end:]
                rd = obj.get("row_data")
                if isinstance(rd, str):
                    try:
                        rd = json.loads(rd)
                    except ValueError:
                        pass
                yield obj.get("source"), rd
            if not chunk:
                break

def peak_mib():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
