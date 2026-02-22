# Reflection: Log Analysis System
1- Where did you choose OO and why?  
- I choice Object_Oriented Programming (OO) for the domain model, specifically the LogEvent dataclass.
- Log data is naturally structured, and using a class allows for:  

  - **Encapsulation:** Grouping the timestamp, level, and metadata into a 
    single unit. 
    and easier to debug.
  - **Validation** Using __post_init__ to ensure that every log entry has a 
    valid level(e.g., INFO, ERROR) before it enters the pipline.
  - **Immutability:** By using a **frozen** dataclass. it makes the system safer 

2- Where did you choose FP and why? 
 - I choice Functional Programming (FP) for the data processing pipline in pipline.py and the analytics queries in queris.py.
 - **Composition:** FP allows us to "chain" operations(e.g., filtering for ERRORs and then counting them) without maintaining complex internal status.
 - **First-Class Functions:** The use of **Dispatch Table** (QUERIES dictionary) treats functions as data. This allows the system to remain flexible and open to new queries without requiring large if/else structures.

3- Which parts are lazy and what benefits does that provide? 
  - The entire ingestion and transformation pipline (read_lines, parse_events, filter_level, and map_messages) is lazy.
    - **Mechanism:** These functions use Python **Generator** (yield) and **Generator Expressions**.
    - **Benifits**: The primary benefit is **memory efficiency** (O(1) space complexity). Because we process logs one line at a time rather than loading the entire file into a list.

4- A place where you intentionally avoided over-abstraction (and why)?
  - I intentionally avoided creating a "Query Manager" or "Log Processor" class for execution logic.

    - **Whay:** While I could have used the **Command Pattern** or **Inheritance** to define queries, it would have added unnecessary "boilerplate" code.
    Instead, I used a simple Dispatch Table (a dictionary of functions). This provides the same extensibility as complex OO patterns but keeps the code much more readable and easier to test.


