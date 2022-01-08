# LinkedList
Custom Linked List implementation for data structures practice. Constructor takes in an optional array of int values and converts them to a series of Node objects. Node contains a "data" value and a "next" reference.

### Note:
The array parameter type is a little weird when dealing when lists with a single node. The main reason I chose this was to avoid having to spam listname.append() when populating a LinkedList with values, which occcurs far more often than creating a list with a single value. Most algorithms will work with Node objects anyway so this shouldn't be a problem.