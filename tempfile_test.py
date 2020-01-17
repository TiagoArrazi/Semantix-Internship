import tempfile 


tmp = tempfile.NamedTemporaryFile(mode='a')
print(tmp.name)
input()
tmp.close()
