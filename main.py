
def loop():
    # init vars
    LRU = False
    FIFO = False
    pageframes = []
    inp = None
    totalreqs = 0
    hits = 0
    while inp != 'exit':
        inp = input('What algorithm would you like to use, LRU or FIFO? Enter exit to close the program.\t')
        if inp.upper() != 'EXIT':
            if inp.upper() == 'LRU':
                LRU = True
            else:
                FIFO = True

            pageno = input('How many page frames would you like?\t')
            while not pageno.isdecimal():
                pageno = input('You need to specify a number of page frames as an integer. Try again.')
            while not int(pageno) > 1:
                pageno = input('The number of page frames needs to be larger than 1. Try again.')
            # add page frames
            for x in range(int(pageno)):
                pageframes.append([x, None, ''])
                print(f'Adding page frame {x}...')
            print('Page Frame\t\tCurrent Page\t\tInterrupt\n==============================')
            for page in pageframes:
                print(f'\t{page[0]}\t\t|\t\t{page[1]}\t\t|\t\t{page[2]}')
            # FIFO list for which to replace next
            fifo = []
            # LRU list for which to replace next
            lru = []
            # frame to be called
            framecall = ''

            while framecall.upper() != 'EXIT':

                framecall = input('What frame do you want to request?\t')

                while framecall == '' or framecall is None:
                    framecall = input('There was an error processing that request, please try again.')

                # if we need to use logic or not to insert the new call
                flag = False
                # total requests
                totalreqs += 1
                if framecall.upper() != 'EXIT':
                    # remove all interrupt markers for this cycle
                    for page in pageframes:
                        page[2] = ''

                    for x in range(len(pageframes)):
                        # frame is already loaded
                        if framecall in pageframes[x]:
                            hits += 1
                            flag = True

                            lru.remove(x)
                            lru.append(x)
                            print(f'Page {framecall} is already loaded, no interrupt occurs.')
                            break

                        # frame is not loaded and spot is open (goes into first available spot)
                        elif None in pageframes[x]:
                            print(f'Inserting page {framecall} into empty page frame {x}...')
                            pageframes[x] = [x, framecall, '*']
                            fifo.append(x)
                            lru.append(x)
                            flag = True
                            break

                    # figure out LRU or FIFO here
                    if not flag and LRU:
                        ind = lru.pop(0)
                        print(
                            f'Removing page {pageframes[ind][1]} at page frame {ind} and inserting page {framecall}...')
                        pageframes[ind] = [ind, framecall, '*']
                        lru.append(ind)
                    elif not flag and FIFO:
                        ind = fifo.pop(0)
                        print(
                            f'Removing page {pageframes[ind][1]} at page frame {ind} and inserting page {framecall}...')
                        pageframes[ind] = [ind, framecall, '*']
                        fifo.append(ind)
                print('Page Frame\t\tCurrent Page\t\tInterrupt\n=============================================')
                for page in pageframes:
                    print(f'{page[0]}\t\t|\t\t{page[1]}\t\t\t|\t\t{page[2]}')
                print(f'Current Failure Rate: {"{:.3f}".format(float((totalreqs - hits) / totalreqs) * 100)}%\nHits: {hits}\nTotal Requests: {totalreqs}')


if __name__ == '__main__':
    loop()
