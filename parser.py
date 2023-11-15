from knowledge_base import Fact, Rule


class Parser:
    @staticmethod
    def parse_fact_line(fact):
        return Fact(fact.rstrip().strip().split())

    @staticmethod
    def parse_facts(filename):
        with open(filename, 'r') as file:
            return [Parser.parse_fact_line(line) for line in file]

    @staticmethod
    def parse_rule(lhs, rhs):
        return Rule([[list(map(lambda x: x.strip(), c)) for c in lhs], rhs])

    @staticmethod
    def parse_rule_line(line):
        r = line.split('->')
        rhs = r[1].rstrip().strip().split()
        lhs = r[0].split('&')
        lhs = map(lambda x: x.rstrip().strip().split(), lhs)
        return Parser.parse_rule(lhs, rhs)

    @staticmethod
    def parse_rules(filename):
        with open(filename, 'r') as file:
            lines = [line.rstrip() for line in file]
        rules = []
        for line in lines:
            r = line.split('->')
            rhs = r[1].rstrip().strip().split()
            lhs = r[0].split('&')
            lhs = map(lambda x: x.rstrip().strip().split(), lhs)
            rules.append(Parser.parse_rule(lhs, rhs))
        return rules
