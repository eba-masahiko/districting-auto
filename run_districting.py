from functools import partial
from gerrychain import Graph, Partition, MarkovChain
from gerrychain.proposals import recom
from gerrychain.constraints import within_percent_of_ideal_population
from gerrychain.accept import always_accept
from src.config import TARGET_DISTRICTS, POP_TOLERANCE

def run_districting(gdf, graph):
    ideal_pop = gdf["population"].sum() / TARGET_DISTRICTS
    assignment = {n: n % TARGET_DISTRICTS for n in graph.nodes()}
    initial_partition = Partition(graph, assignment=assignment,
                                  updaters={"population": lambda p: sum(gdf.loc[list(p), "population"])})
    proposal = partial(recom, pop_col="population", pop_target=ideal_pop, epsilon=POP_TOLERANCE)
    chain = MarkovChain(
        proposal=proposal,
        constraints=[within_percent_of_ideal_population(initial_partition, POP_TOLERANCE)],
        accept=always_accept,
        initial_state=initial_partition,
        total_steps=200,
    )
    best = min(chain, key=lambda p: max(p["population"].values()) / min(p["population"].values()))
    return best
