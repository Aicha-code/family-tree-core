``Family Tree Core``

## Overview

Family Tree Core is a Python domain-level implementation of a family tree / kinship modeling system.

This repository focuses exclusively on the core data structures, relationships, and algorithms required to model family relationships such as:
- parents
- children
- spouses
- siblings
- cousins
- grandparents
- extended kinship

The system is intentionally built without any dependency on databases, frameworks, or user interfaces.

The goal is to design a clean, privacy-first, and culturally flexible foundation that can later be integrated into different applications (CLI tools, Django apps, research tools, etc.).

## Motivation

This project originated from a personal and cultural need to model Family Heritage accurately, particularly because:

- Families are large (many siblings)
- Extended kinship relationships are common
- Certain marriage constraints exist (e.g. no direct cousin marriage)
- Privacy and data sensitivity are critical

Rather than starting with a web app or database, this repository prioritizes correct modeling and reasoning about family relationships.

## Scope of This Repository

### Included

Core domain model (`Member`)

Family graph coordinator (`FamilyTree`)

Parent–child relationships

Marriage and divorce logic

Bidirectional relationship consistency

Derived kinship algorithms:


- siblings
- full siblings
- half siblings
- uncles and aunts
- cousins
- grandparents

In-memory family graph structure

Relationship validation rules

### Explicitly Excluded

Databases (SQLite, PostgreSQL, etc.)

Web frameworks (Django, FastAPI, Flask)

Authentication or authorization

Public APIs

User interfaces (web or mobile)

These will be handled in separate repositories once the core logic is stable.

## Architecture

The system currently consists of two primary abstractions:

### Member
Represents an individual and maintains local relationship state
(parents, children, spouses).

Members act as **nodes in the family graph**.

### FamilyTree
Acts as the graph coordinator responsible for:

- member creation
- relationship validation
- structural queries
- kinship derivation

## Design Principles

Logic first: domain modeling before persistence

Privacy by design: no real data committed, no public exposure

Derived relationships: siblings and cousins are computed, not stored

Framework-agnostic: pure Python, no external dependencies

Extensible: designed to support multiple marriages, large families, and complex kinship graphs

## Current Status

The core kinship model is now implemented and supports:

- marriage and divorce
- parent–child relationships
- sibling derivation
- extended kinship queries
- multi-generation traversal

The current focus is improving:

- graph traversal algorithms
- relationship queries
- testing scenarios

The internal structure may evolve as understanding deepens.

---
## Example Relationships Supported

The system can currently derive:

Child → Parents  
Parent → Children  
Sibling relationships  
Half-siblings vs full siblings  
Uncles and aunts  
Cousins  
Grandparents

All relationships are computed dynamically from the family graph.
---

## Planned Extensions (Future Work)

Ancestor traversal

Descendant traversal

Kinship distance calculation

Cycle-safe graph operations

Family lineage queries


Integration with:

- A Django-based backend

- A private local database

- Visualization tools

## Ethical & Privacy Considerations

This project is intentionally developed as private-first:

No real family data is included in this repository  

No public database is assumed

## Running the Demo

To run the example family tree:

python demo.py