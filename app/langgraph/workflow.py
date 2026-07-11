from langgraph.graph import StateGraph, END

from app.langgraph.state import GraphState
from app.langgraph.router import QueryRouter
from app.langgraph.nodes import WorkflowNodes


class AeroWorkflow:

    def __init__(self):

        # ----------------------------------------
        # Services
        # ----------------------------------------

        self.router = QueryRouter()

        self.nodes = WorkflowNodes()

        # ----------------------------------------
        # Create LangGraph
        # ----------------------------------------

        self.workflow = StateGraph(GraphState)

        # ----------------------------------------
        # Register Nodes
        # ----------------------------------------

        self.workflow.add_node(
            "router",
            self.route_node
        )

        self.workflow.add_node(
            "metadata",
            self.nodes.metadata_node
        )

        self.workflow.add_node(
            "vector",
            self.nodes.vector_node
        )

        self.workflow.add_node(
            "graph",
            self.nodes.graph_node
        )

        # ----------------------------------------
        # Entry Point
        # ----------------------------------------

        self.workflow.set_entry_point(
            "router"
        )

        # ----------------------------------------
        # Conditional Routing
        # ----------------------------------------

        self.workflow.add_conditional_edges(
            "router",
            self.route_decision,
            {
                "metadata": "metadata",
                "vector": "vector",
                "graph": "graph"
            }
        )

        # ----------------------------------------
        # End Nodes
        # ----------------------------------------

        self.workflow.add_edge(
            "metadata",
            END
        )

        self.workflow.add_edge(
            "vector",
            END
        )

        self.workflow.add_edge(
            "graph",
            END
        )

        # ----------------------------------------
        # Compile Graph
        # ----------------------------------------

        self.app = self.workflow.compile()

    # ==================================================
    # Router Node
    # ==================================================

    def route_node(self, state: GraphState):

        route = self.router.route(
            question=state["question"],
            scope=state["scope"]
        )

        state["route"] = route

        return state

    # ==================================================
    # Conditional Router
    # ==================================================

    def route_decision(self, state: GraphState):

        return state["route"]
