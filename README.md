# Traffic Route Planner

[![CI](https://github.com/JiayiGu233/traffic-route-planner/actions/workflows/ci.yml/badge.svg)](https://github.com/JiayiGu233/traffic-route-planner/actions/workflows/ci.yml)

**C++17 · Dijkstra · Adjacency lists**

An undirected road-network CLI that finds minimum travel-time routes and responds to changing traffic factors.

## Quick start

```text
make
printf 'insert 1 2 10 5\ninsert 2 3 20 10\npath 1 3\nlowest 1 3\nexit\n' | ./graph.out
```

## Design

Road edges store distance, speed and a traffic adjustment factor. Dijkstra uses a priority queue; edge updates are mirrored in both directions. Vertices and their incident edges can be deleted.

## Scope and validation

Inputs should follow the CLI grammar and use valid nonnegative distances and positive speeds. This is an in-memory algorithm demonstration, not a map-data service.

See [VALIDATION.md](VALIDATION.md) for checks run against this edition. Source background and authorship are recorded in [PROVENANCE.md](PROVENANCE.md).
