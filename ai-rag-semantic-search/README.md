# AI Semantic Search using Endee Vector Database

## Project Overview

This project demonstrates an AI-powered semantic search system using vector embeddings.

The system converts text documents into vector embeddings using a sentence transformer model and retrieves the most relevant document for a user query using similarity search.

This architecture represents the core idea behind modern AI systems such as Retrieval Augmented Generation (RAG), recommendation engines, and intelligent search systems.

## Problem Statement

Traditional keyword search often fails to understand the semantic meaning of queries.

Vector search solves this problem by converting text into numerical embeddings and retrieving results based on semantic similarity rather than exact keyword matches.

## System Architecture

User Query  
↓  
Sentence Transformer (Embedding Model)  
↓  
Vector Embeddings  
↓  
Vector Database (Endee)  
↓  
Similarity Search  
↓  
Top Relevant Result

## Technologies Used

Python  
Sentence Transformers  
Vector Embeddings  
Endee Vector Database  
NumPy

## How Endee is Used

Endee is a high-performance vector database used to store and retrieve embeddings efficiently.

In a production environment, the embeddings generated from documents would be stored inside the Endee vector database. When a user submits a query, the query embedding would be compared with stored embeddings using vector similarity search.

This project demonstrates the core pipeline required to integrate with Endee for scalable AI search systems.

## Setup Instructions

Clone repository

