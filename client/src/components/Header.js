import { useNavigate } from "react-router-dom";
import "./css/Header.css";

export default function Header() {
  return (
    <>
      <div className="links-container">
        <a className="link" href="tel:+74950330363" data-sign="whatsapp">Приемная комисия</a>
        <a className="link" href="tel:+84955000363" data-sign="call">84955000363</a>
        <a className="link" href="tel:+88005500363" data-sign="call">88005500363</a>
        г. Москва
      </div>
      <div className="Header">
        <div className="Logo"></div>
        <div className="Title">Отдел воспитательной работы</div>
      </div>
      <div className="Divider"></div>
      <div className="Button-Container">
        <LinkButton url="/groups">Группы</LinkButton>
        <LinkButton url="/students">Студенты</LinkButton>
        <LinkButton url="/student-council">Студенческий совет</LinkButton>
        <LinkButton url="/teachers">Преподаватели</LinkButton>
        <LinkButton url="/events-list">Список мероприятий</LinkButton>
        <LinkButton url="/events-log">Журнал мероприятий</LinkButton>
        <LinkButton url="/report">Отчет</LinkButton>
      </div>
    </>
  )
}

const LinkButton = ({ children, url=null }) => {
  const navigate = useNavigate();
  return (
    <div className="LinkButton" onClick={() => {navigate(url)}}>
      {children}
    </div>
  )
}