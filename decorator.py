   
import time

def duration_time(function):
    def wrapper():
        init = time.time()
        function()
        final = time.time()
        
        print('O tempo total da função {}: {}'.format(function.__name__, str(final - init)))
    return wrapper
    
@duration_time
def main():
    for i in range(1, 1000000):
        pass
    
main()
