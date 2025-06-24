import reflex as rx

config = rx.Config(
    app_name="solar_comp",
    db_url="sqlite:///solar_marketplace.db",  # SQLite para desenvolvimento local
    env=rx.Env.DEV,
    plugins=[rx.plugins.TailwindV3Plugin()]
)