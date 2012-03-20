from disco.core import Job, result_iterator
from mongoDisco_output import MongoDBoutput
from disco.worker.classic.func import task_output_stream
from mongodb_io import mongodb_output_stream

def map(line, params):
    for word in line.split():
        yield word,1

def reduce(iter, params):
    from disco.util import kvgroup
    for word, counts in kvgroup(sorted(iter)):
        yield word, sum(counts)

'''
def mongodb_output(stream,partition,url,params):
    return mongoDisco_output.MongoDBoutput(stream,params)
'''

if __name__ == '__main__':

    job = Job().run(input=["raw://123 it it it hi hi mi"],
            map=map,
            reduce=reduce,
            reduce_output_stream=mongodb_output_stream)

    job.wait(show=True)
