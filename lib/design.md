Multi-Class Planned Design Recipe

1. As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries


2. Design the Class System
Almost identical to previous exercises (with addition of phone numbers)

Diary > DiaryEntry > Phone (phone numbers can be aditional method in diary rather than class)
TodoList > Tasks

3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.
Encode one of these as a test and move to step 4.

Add multiple diary entries, select appropriate one to read in diary, pull out phone numbers from diary


This is exactly the same as the previous exercises.

4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.
Encode one of these as a test and move to step 5.
This is exactly the same as the previous exercises.

5. Implement the Behaviour


    
        def number_extractor(self):
            
            for entry in self.contents():
                if 0 in entry.contents():
                self.numbers.append()