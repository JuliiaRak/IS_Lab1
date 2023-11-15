import sys

from parser import Parser
from knowledge_base import KnowledgeBase


def main():
    knowledge_base = KnowledgeBase()
    reader = Parser()

    facts = reader.parse_facts(sys.argv[1])
    knowledge_base.add_facts(facts)

    rules = reader.parse_rules(sys.argv[2])
    knowledge_base.add_rules(rules)

    while True:
        line = input()

        if line == 'exit':
            break
        else:
            fact = Parser.parse_fact_line(line)
            bindings = knowledge_base.query(fact)
            if bindings:
                for binding in bindings:
                    print(str(binding))
            else:
                print('There is no true statements')


if __name__ == "__main__":
    main()
