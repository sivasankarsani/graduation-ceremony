from itertools import permutations


class GraduationCeremony:
    def __init__(self, no_of_days, minimum_days_to_attend=4):
        if no_of_days < 4:
            raise Exception('Nth day should be more than 3')

        self.no_of_days = no_of_days
        self.minimum_days_to_attend = minimum_days_to_attend

        self.init()

    def init(self):
        self.invalid_ways = {}
        '''
        Ways to attend
        nc0 + nc1 + nc2 + nc3 + nc4 + nc5 >> 2 pow(n)
        where n=nth day
        '''
        self.total_no_ways = 2 ** self.no_of_days

        '''
        Student should be present on Nth day ow irrespective of attend classes, won't be allowed.
        ways to miss ceremony: 2 pow(n-1)
        '''
        self.total_ways_to_miss = 2 ** (self.no_of_days -1)

        self.no_of_ways_to_attend_class()

    def no_of_ways_to_attend_class(self):
        self.invalid_ways = {
            ( ('0',) * self.no_of_days):1
        }
        '''
        We need to find out all invalid days(consecutive days) of total_no_ways.
        ex:
        N=5
        5c0 + 5c1 + 5c2 + 5c3 + 5c4 + 5c5
        0 present + 1 present + 2 present + ....

        Here 1 present meant that there can be possible of consecutive days like
        a.a.a.a.a + p.a.a.a.a + a.a.a.a.p >> 3

        assume that 1 is present days and 0 is absent days.
        '''

        possible_ways_to_present = self.no_of_days - self.minimum_days_to_attend

        for p_day in range(1, possible_ways_to_present+1):
            absent_days = self.no_of_days - p_day
            choices = '1'* p_day + '0' * absent_days
            perms = set(permutations(choices))

            for perm in perms:
                itert_counts = self.no_of_days - self.minimum_days_to_attend - p_day  + 1
                stop_iter = False
                for count in range(itert_counts):
                    consecutive_absent_days=step = self.no_of_days - p_day - count
                    limit = p_day + count + 1
                    for index in range(limit):
                        sub_str = perm[index: index + step]
                        if sub_str.count('0') == consecutive_absent_days:
                            self.invalid_ways[perm] = self.invalid_ways.get(perm, 0) + 1
                            stop_iter = True
                            break
                    if stop_iter:
                        break

        no_of_ways_to_attend = self.total_no_ways - len(self.invalid_ways)

        self.no_of_ways_to_miss_ceremony(no_of_ways_to_attend)

    def no_of_ways_to_miss_ceremony(self, no_of_ways_to_attend):
        '''
        Ex: 5
        x.x.x.x.a where x is either present(1) or absent(0).
        2**n-1 - remove all invalid days(consecutive days) whose appear on Nth day absent.
        '''
        invalid_consecutive_days = sum(1 for way in self.invalid_ways if way[-1]=='0')
        probability = self.total_ways_to_miss - invalid_consecutive_days
        print(f'{probability}/{no_of_ways_to_attend}')


if __name__ == '__main__':
    no_of_days = int(input())
    GraduationCeremony(no_of_days)

