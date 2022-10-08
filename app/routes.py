import flask
from app import flask_app, db
from app.forms import RegisterForm, NewCrop, SignInForm, HarvestForm, ContactForm
from app.models import Users, Harvests, Crops
from app.weather import TodayCondition
# import flask_login


@flask_app.route("/")
def homepage():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        name = contact_form.name.data
        email = contact_form.contact_address.data
        message = contact_form.message.data
    return flask.render_template("homepage.html", contact_form=contact_form)


@flask_app.route("/dashboard", methods=["GET", "POST"])
def dashboard_page():
    today_date = TodayCondition.get_date()
    average_temperature = TodayCondition.average_temp()
    amount_rainfall = TodayCondition.amount_precipitation()
    condition_weather = TodayCondition.condition_weather()

    new_crop = NewCrop()
    print("Form")
    if new_crop.validate_on_submit():
        crop_name = new_crop.crop_name.data
        sow_date = new_crop.sow_date.data

        da_list = [crop_name,
                   sow_date]
        print(da_list)

        crops = Crops(
            crop_name=crop_name,
            sow_date=sow_date,
        )

        db.session.add(crops)
        db.session.commit()

        return flask.redirect("/homepage")
    else:
        print("Wrong outcome")

    return flask.render_template("dashboard-content.html",
                                 new_crop=new_crop,
                                 today_date=today_date,
                                 average_temperature=average_temperature,
                                 amount_rainfall=amount_rainfall,
                                 condition_weather=condition_weather)


@flask_app.route("/harvest")
def harvest_page():
    harvest_form = HarvestForm()

    if harvest_form.validate_on_submit():
        harvest_date = harvest_form.harvest_date.data
        quantity = harvest_form.quantity.data
        units = harvest_form.units.data

        harvests = Harvests(
            harvest_date=harvest_date,
            quantity=quantity,
            units=units,
        )

        db.session.add(harvests)
        db.session.commit()

    return flask.render_template("harvest.html", harvest_form=harvest_form)


# @login_manager.user_loader
# def load_user(Id):
#     Id = int(Id)
#     return models.Users.get(Id)


@flask_app.route("/register", methods=["GET", "POST"])
def register_page():

    login_form = SignInForm()
    register_form = RegisterForm()

    if login_form.validate_on_submit():
        print("Successfully log in ")

    if register_form.validate_on_submit():
        f_name = register_form.first_name.data
        l_name = register_form.last_name.data
        email_address = register_form.email_address.data
        pwd = register_form.password.data
        c_pwd = register_form.password.data
        print(c_pwd)
        if c_pwd == c_pwd:
            print("Under progress for confirm password")

        users = Users(
            first_name=f_name,
            last_name=l_name,
            email_address=email_address,
            password=pwd
        )

        db.session.add(users)
        db.session.commit()

        print("ADDING TO DATABASE")

        return flask.redirect("/")

    return flask.render_template('signin.html', login_form=login_form, register_form=register_form)


# @flask_app.route('/logout')
# def logout():
#     flask_login.logout_user()
#     return flask.redirect("/")
