class ReplayCounter():

    def __init__(self):
        self.return_codes_count = dict()
        self.host_count = dict()

    def return_code_counter(self, code):
        if code in self.return_codes_count:
            self.return_codes_count[code] += 1
        else:
            self.return_codes_count[code] = 1

    def request_host_counter(self, host):
        if host in self.host_count:
            self.host_count[host] += 1
        else:
            self.host_count[host] = 1

    def hosts_print_report(self):
        for k, v in self.host_count.iteritems():
            print k, v

    def codes_print_report(self):
        for k, v in self.return_codes_count.iteritems():
            print k, v
