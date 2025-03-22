from datetime import date

import reflex as rx

from personal_web.data.job import Company, Job
from personal_web.state import MainState
from personal_web.styles import styles
from personal_web.styles.colors import TextColor
from personal_web.styles.styles import Size


def company_experience(company: Company, en: bool = False) -> rx.Component:
    present_word = "present" if en else "actualidad"
    end_date = (
        company.end_date.strftime("%b. %Y") if company.end_date < date.today() else present_word
    )
    return rx.vstack(
        rx.hstack(
            rx.link(
                rx.tooltip(
                    rx.image(
                        src=company.company_logo,
                        alt=company.company_name,
                        width=rx.breakpoints(
                            initial="4em",
                            md="5em",
                            lg="6em",
                        ),
                        height=rx.breakpoints(
                            initial="4em",
                            md="5em",
                            lg="6em",
                        ),
                        padding="0.2em",
                        transition="transform 0.2s ease",
                        _hover={
                            "transform": "scale(1.1)",
                        },
                    ),
                    content=(
                        f"Go to {company.company_name} website"
                        if en
                        else f"Ir al sitio web de {company.company_name}"
                    ),
                    side_offset=-5,
                ),
                is_external=True,
                href=company.company_url,
                _hover={"cursor": "pointer"},
            ),
            rx.divider(orientation="vertical", height="4.5em", border="0.3px solid #E2E8F0"),
            rx.vstack(
                rx.heading(company.company_name, size=rx.breakpoints(initial="6", md="7")),
                rx.text(
                    f"{company.start_date.strftime('%b. %Y')} -  {end_date}",
                ),
            ),
            spacing="5",
            align="center",
        ),
        rx.divider(color_scheme="red"),
        rx.accordion.root(
            *[job_experience(job, en) for job in company.jobs],
            width="100%",
            variant="ghost",
            collapsible=True,
            color_scheme="gray",
            padding_left=rx.breakpoints(
                initial="0.5em",
                md="1.5em",
                lg="2em",
            ),
            radius="large",
            type="multiple",
        ),
        width="100%",
    )


def job_experience(job: Job, en: bool = False) -> rx.Component:
    present_word = "present" if en else "actualidad"
    end_date = job.end_date.strftime("%b. %Y") if job.end_date <= date.today() else present_word
    return rx.accordion.item(
        header=rx.vstack(
            rx.heading(
                job.title,
                size=rx.breakpoints(
                    initial="5",
                    md="6",
                ),
                align="left",
            ),
            rx.text(
                f"{job.start_date.strftime('%b. %Y')} -  {end_date}",
                color_scheme="red",
            ),
            align="start",
        ),
        content=job_experience_content(job),
        color=TextColor.PRIMARY.value,
    )


def job_experience_content(job: Job) -> rx.Component:
    return rx.vstack(
        rx.cond(
            job.description,
            rx.heading(
                rx.cond(
                    MainState.is_language_en,
                    "📋 Main Function",
                    "📋 Función principal",
                ),
                size=rx.breakpoints(
                    initial="4",
                    md="5",
                ),
            ),
        ),
        rx.cond(
            job.description,
            rx.text(
                job.description,
                text_align="justify",
                size=rx.breakpoints(
                    initial="2",
                    md="4",
                ),
            ),
        ),
        rx.cond(
            job.achievements,
            rx.heading(
                rx.cond(
                    MainState.is_language_en,
                    "🏆 Achievements",
                    "🏆 Logros",
                ),
                size=rx.breakpoints(
                    initial="4",
                    md="5",
                ),
            ),
        ),
        rx.cond(
            job.achievements,
            rx.text(
                job.achievements,
                text_align="justify",
                size=rx.breakpoints(
                    initial="2",
                    md="4",
                ),
            ),
        ),
        rx.cond(
            len(job.technologies) > 0,
            rx.flex(
                *[tech_badge(name) for name in job.technologies],
                padding_top=Size.DEFAULT_MEDIUM.value,
                padding_bottom=Size.ZERO.value,
                spacing="0",
                flex_wrap="wrap",
            ),
        ),
        padding_left=rx.breakpoints(
            initial="0.5em",
            md="1.5em",
            lg="2em",
        ),
        align_items="start",
    )


def tech_badge(tech_name: str) -> rx.Component:
    return rx.badge(tech_name, style=styles.TECH_BADGE_STYLE)
