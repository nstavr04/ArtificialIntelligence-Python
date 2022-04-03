from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment

        variable = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(variable, assignment):
            if self.is_consistent(variable, value, assignment):
                assignment[variable] = value
                result = self.recursive_backtracking(assignment)
                if result is not False:
                    return result
                del assignment[variable]
        return False

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_sa_csp():
    cr, pan, col, ven, ecu, guy, sur, guyfr, peru, brasil, bol, para, argen, uru, chile = 'CR', 'PAN', 'COL', 'VEN', 'ECU', 'GUY', 'SUR', 'GUYFR', 'PERU', 'BRAZIL', 'BOL', 'PARA', 'ARGENTINA', 'URU', 'CHILE'
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [cr, pan, col, ven, ecu, guy, sur, guyfr, peru, brasil, bol, para, argen, uru, chile]
    domains = {
        cr: values[:],
        pan: values[:],
        col: values[:],
        ven: values[:],
        ecu: values[:],
        guy: values[:],
        sur: values[:],
        guyfr: values[:],
        peru: values[:],
        brasil: values[:],
        bol: values[:],
        para: values[:],
        argen: values[:],
        uru: values[:],
        chile: values[:],
    }
    neighbours = {
        cr: [pan],
        pan: [cr, col],
        col: [pan, ven, ecu, peru, brasil],
        ven: [col, brasil, guy],
        ecu: [col, peru],
        guy: [ven, sur, brasil],
        sur: [guy, guyfr, brasil],
        guyfr: [sur, brasil],
        peru: [ecu, col, brasil, bol, chile],
        brasil: [guyfr, sur, guy, ven, col, ecu, peru, bol, para, argen, uru],
        bol: [brasil, para, chile, argen, peru],
        para: [brasil, bol, argen],
        argen: [chile, uru, brasil, para, bol],
        uru: [argen, brasil],
        chile: [argen, bol, peru]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        cr: constraint_function,
        pan: constraint_function,
        col: constraint_function,
        ven: constraint_function,
        ecu: constraint_function,
        guy: constraint_function,
        sur: constraint_function,
        guyfr: constraint_function,
        peru: constraint_function,
        brasil: constraint_function,
        bol: constraint_function,
        para: constraint_function,
        argen: constraint_function,
        uru: constraint_function,
        chile: constraint_function
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    sa = create_sa_csp()
    result = sa.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/sa.html
