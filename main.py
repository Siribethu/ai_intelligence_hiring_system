from agents.ceo_agent import CEOAgent


def main():
    ceo = CEOAgent()
    results = ceo.run()

    print("\n🏆 Final Ranking:\n")

    for company, data in results.items():
        print(f"{company}: {data['score']}")
        print(f"   ➤ Reason: {data['reason']}\n")


if __name__ == "__main__":
    main()