import logging


class Core():
    def __init__(self,logger = None):
        self.logger = logger if logger is None else logging
    
    def run(self,input):
        #self.logger.info(f"input: {input} ")
        self.logger.info({"input": input})
        total_score = input['score']+sum([attr['x1'] for attr in input['attr']])
        res = {"predict":str(total_score)}
        #self.logger.info(f"output: {res} ")
        self.logger.info({"output": res})
        return res
