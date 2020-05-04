from app import lib

def dequeue_times(queue, n_times):
    c = None
    for i in range(n_times):
        c = fila.dequeue()
    return c

text = "ojRggcfEtScraPeoOukeSzwtTeAof-dbCobtEqrRjtTsmfsluA"
steps = [3, 5, 2, 4, 3, 4, 4, 2, 3, 3, 4, 3, 3, 7]
fila = lib.Queue(False)

for c in text:
    fila.enqueue(c)

result = ""
for step in steps:
    result += dequeue_times(fila, step)

print(result)