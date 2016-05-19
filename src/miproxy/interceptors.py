import re


class InterceptorPlugin(object):

    def __init__(self, server, msg):
        self.server = server
        self.message = msg


class RequestInterceptorPlugin(InterceptorPlugin):

    def do_request(self, data):
        return data


class ResponseInterceptorPlugin(InterceptorPlugin):

    def do_response(self, data):
        return data


class InvalidInterceptorPluginException(Exception):
    pass


class DebugInterceptor(RequestInterceptorPlugin, ResponseInterceptorPlugin):

    def do_request(self, data):
        print '>> %s' % repr(data[:100])
        return data

    def do_response(self, data):
        print '<< %s' % repr(data[:100])
        return data


class QAReplayInterceptor(RequestInterceptorPlugin, ResponseInterceptorPlugin):

    def do_request(self, data):
        pattern = re.compile('Host: ([\w\.]+)')
        host = pattern.search(data)
        if host:
            replay_counter.request_host_counter(host.group(1))
        return data

    def do_response(self, data):
        pattern = re.compile('^HTTP/1.1 (\d{3}) .*')
        return_code = pattern.search(data)
        if return_code:
            replay_counter.return_code_counter(return_code.group(1))
        return data


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

    def report_qa_replay_metrics(self):
        print "Host Requests distribution:\n"
        self.hosts_print_report()
        print "##################################\n"
        print "Codes Responses distribution:\n"
        self.codes_print_report()


replay_counter = ReplayCounter()
