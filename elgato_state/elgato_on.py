import asyncio

from elgato import Elgato, State, Info


async def main():
    """Show example on controlling your Elgato Light device."""
    async with Elgato("192.168.1.221") as elgato:
        info: Info = await elgato.info()
        print(info)

        state: State = await elgato.state()
        print(state)

        # Turn the light on
        await elgato.light(on=True)


if __name__ == "__main__":
    asyncio.run(main())
