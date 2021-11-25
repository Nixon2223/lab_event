# Lab - Event 

## Task

The task for this lab is to plan and create an object oriented model of an Event, with Performers and Customers! You should write tests for all your classes and methods. Make sure that you create a separate file for each class and a separate test file for each class.

## Learning Objectives

1. Create your own classes
2. Create multiple objects
3. Add some properties
4. Add some methods and behaviours
5. Get methods and behaviours to interact with properties
6. Get classes to interact with each other
7. Test classes and methods

### Files and Directories

  - In your working directory, create two directories, one for your classes and one for your tests
  - Remember to create an empty `__init__.py` file in the directories created above
  - create a `run_tests.py` file in your working directory. Use this file to run your tests.
  - If a method returns a boolean i.e. `True` or `False` then create _at least_ two tests for the method, one where you expect the result to be `True`, and one where you expect the result to be `False`

**REMEMBER** to commit to git regularly

### MVP:

  - An `Event` should have a `name`, a `ticket_price`, a `revenue` starting from 0, a list of `customers` and a list of `performers`
  - A `Performer` should have a `name` and `earnings` that start from 0
  - A `Customer` should have a `name`,`wallet` and a `favourite_performer`
  - An `Event` should be able to sell a ticket to a `Customer`, adding them to its list of `customers`, reducing money in their `wallet` and increasing the `Event`s `revenue`. Make sure the `Customer` has enough money to purchase a  ticket.
  - An `Event` should be able to add to its `customers` and `performers`. Make sure there are no duplicates on the list
  - An `Event` should also be able to tell if a `Customer`'s `favourite_performer` is on its list of `performers`
  - An `Event` should be able to book a `Performer`, adding it to its list of performers, reducing its `revenue` and increasing the `Performer`'s `earnings`.

### Extensions:

  - Add an age restriction to the `Event` and an age property to the `Customer`. When selling a ticket to a `Customer`, check their age before allowing the sale to happen.
  - When `Customer` buys a ticket, divide 50% of ticket price between all of the `Event`s `performers` and give remaining 50% to `Event`.
  - Allow `Customer`s and `Performer`s to cancel their attendance, along with refunds for any tickets and earnings to be made.