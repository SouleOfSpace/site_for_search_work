class Searcher():
    def get_destroed_requests(self, tracker):
        '''Разбивает полученный трэкер на части по разделителям и собирает их всех в массив'''
        destroed_tracker = []
        barriers = [' ',';', ',','',]
        line = ''

        for symbole in tracker:
            line += symbole

            for barrier in barriers:
                if symbole == barrier and line.strip() in barriers:
                    line = line[0:-1]
                    break
                if symbole == barrier:
                    destroed_tracker.append(line[0:-1])
                    line = ''
                    break

        destroed_tracker.append(line)
        return destroed_tracker

print(Searcher().get_destroed_requests('    ')==[''])
