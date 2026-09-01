# Strips the document wrapper so a page can be published as an Artifact (which
# supplies its own <!doctype>/<html>/<head>/<body>), and inlines local images as
# data URIs, since the Artifact CSP blocks every external image host.
#   python build-artifact.py index.html out.html
import io, os, re, sys, base64, mimetypes

src, dest = sys.argv[1], sys.argv[2]
s = io.open(src, encoding="utf-8").read()

out = []
for line in s.splitlines():
    t = line.strip().lower()
    if t.startswith(("<!doctype", "<html", "<head>", "</head>", "<body>", "</body>", "</html>",
                     "<meta charset", '<meta name="viewport"', '<meta name="description"')):
        continue
    out.append(line)
s = "\n".join(out) + "\n"

cache = {}
def datauri(path):
    if path not in cache:
        mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
        cache[path] = "data:%s;base64,%s" % (mime, base64.b64encode(open(path, "rb").read()).decode())
    return cache[path]

for path in sorted(set(re.findall(r'bilder/[A-Za-z0-9._-]+', s))):
    if os.path.exists(path):
        s = s.replace(path, datauri(path))
        print("  inlined", path)

io.open(dest, "w", encoding="utf-8").write(s)
print("wrote", dest, round(len(s)/1024), "KB")
