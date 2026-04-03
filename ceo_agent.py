from agents.data_agent import load_jobs
from agents.signal_agent import detect_signals
from agents.scoring_agent import score_companies


class CEOAgent:

    def run(self):
        print("\n🧠 CEO Agent: Starting system...\n")

        df = load_jobs()
        signals = detect_signals(df)
        results = score_companies(signals)

        return results