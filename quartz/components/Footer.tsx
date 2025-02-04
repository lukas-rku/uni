import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/footer.scss"
import { version } from "../../package.json"
import { i18n } from "../i18n"

interface Options {
  links: Record<string, string>
}

export default ((opts?: Options) => {
  const Footer: QuartzComponent = ({ displayClass }: QuartzComponentProps) => {
    return (
      <footer class={`${displayClass ?? ""}`}>
        <hr class="footer-hr"></hr>
        <p style="display: flex; gap: 10px; align-items: center;">
          <a href="https://github.com/lukas-rku/uni">
            <img src="https://img.shields.io/github/last-commit/lukas-rku/uni?label=Last%20Update&color=8556cc" alt="GitHub Last Commit Badge" />
          </a>
          <a href="https://quartz.jzhao.xyz/">
            <img src="https://img.shields.io/badge/Made_using-Quartz-8556cc" alt="Made using Quartz Badge" />
          </a>
          <a href="https://github.com/lukas-rku/uni">
            <img src="https://img.shields.io/badge/GitHub-Repository-8556cc" alt="GitHub Repository Badge" />
          </a>
        </p>
      </footer>
    )
  }

  Footer.css = style
  return Footer
}) satisfies QuartzComponentConstructor


