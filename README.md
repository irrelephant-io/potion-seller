# Potion Seller
An in-depth description of the Potion Seller inventory management system

For additional information, please refer to the instructional video hosted [here](https://www.youtube.com/watch?v=R_FQU4KzN7A).

## On the serious note
A wizarding fella (codename Potion Seller) has reached out to our consultancy firm a few days ago, asking to build a prototype for his new inventory management system. We currently don't have much capacity to implement a fully automated potion warehousing solution for him, but he is running a small shop in the neighbouring town, and as such, would be completely satisfied with a prototype for one.

If he is satisfied with the POC for this system, he is likely going to conjure up enough gold for us to finally afford an AWS subscription!

## Requirements
He was very vague about the exact details of his (honestly pretty shady) business. We only managed to extract a few requirements for this new system from him, but it should be enough to build a POC out of. Here are the bits of insight that he had provided us with:

### User Requirements
These are the requirements we got from our client. We need to make sure these are in accord with what we can achieve technically (See Technical Requirements later in the document).

1. **Potion Seller is an old-school UNIX wizard, so he prefers to work with the terminal whenever possible.**
You need not to concern yourself with GUI for this system as we already have managed to procure an expert in `ncurses` to build an amazing terminal-driven user interface. Your job is to deliver the meat and potatoes - the actual inventory management logic.

2. **System must keep stock of all potions that are currently available in the shop**.
Having a note of the stock is very important as it will allow the the shop to adjust to the demand and brew more of the popular potions when necessary.

3. **System must keep stock of all potion ingredients available for brewing**.
This will allow the shop to send elves out to procure more when needed.

4. **System must be able to figure out if it is possible to brew a certain potion with a the current stock of ingredients**.
We know that there is a recipe bank that we can import from the shop's SharePoint. We need to develop an algorithm which would produce a response of how many potions of a given type it is possible to brew with the given stock. If it is impossible to brew even one, we need to know how many of the required ingredients we are missing.

5. **System must be able to produce labels for potions**.
Given a certain potion, we need to be able to print out a label for it. The label must include a few pieces of information.

5. **Labels must include the common side effects and potential allergic reactions to a given potion based on the ingredients**.
Every ingredient has its potential side effects and not everyone is good with every ingredient. According to the latest regulations implemented by the Adventurer's Healthcare Association, we must label every potion with this information.

6. **Labels must have an adequate cost for a given potion based on the recipe and current price of ingredients**.
Ingredients and labour all have costs. If we want the Potion Seller to pay for our services, we need to make sure that the client generates an appropriate premium from selling their products.

### Technical Requirements
These are the limitations we have to work with based on how we can integrate with the Potion Seller's current infrastructure:

1. Details of ELF

All current stock information is coming into the system through an old alchemical coal-powered computer their shop has in the basement. It emits individual inventory lines that are present in the shop and is not capable of grouping the results in any sensible way. As such we expect all input to be jumbled up. And it is our job to sort it appropriately.

We have inherited a legacy system from the Potion Seller in a form of the "Enumerator of Labeled Flasks" a.k.a. `elf`. This module will read and yield out all of the items of stock available in the shop's basement in the following form:
```json
[
  { "type": "i", "id": "8c17b4cb" },
  { "type": "p": "id": "73126d4d" },
  { "type": "p": "id": "25d7e6f1" },
  ...the list goes on and on
]
```
We need to build the available stock information out of this data to satisfy the user requirements.

Our understanding is that `type` refers to the type of the item. `i` stands for "ingredient" and `p` stands for "potion".
**We don't know if there are other types of items available but the system is old and faulty, so we need to defend against
poor-quality data.**

`id` property refers to a well-known ID listed in the "Alchemical Brewer's Compendium" a.k.a. `abc`.
This is a third-party system that can, given the ID, tell us more information about the given potion or an ingredient.
We don't know the details of that integration, so you will need to investigate it further.

2. About `elf` and `abc` integrations.

We had already investigated the connectivity with the dependencies and have produced the python modules for you to work with. You need to analyse their behaviour through some exploratory testing.

3. Final API.

We expect you to produce a module that would have the functionality satisfying the user requirements. The implementation of the module is up to you, but we would need some documentation on the public interface of it.

Note about the stock functions:

We want the results to be aggregated for ease of display, so avoid returning duplicate entries. When possible, aggregate potions and ingredients and show their counts.
