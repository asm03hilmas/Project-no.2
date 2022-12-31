class menu:

    search_menu = "//input[@placeholder='Search']"

    list_menu = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul//a'


class key_data():
    search_admin = "Admin"
    search_pim = " pim"
    search_leave = "Leave"
    search_time = "Time"
    search_recur = "Recruitment"
    search_my = "My Info"
    search_perf = "Performance"
    search_dash = "Dashboard"
    search_dirc = "Directory"
    search_main = "Maintenance"
    search_Buz = " buzz"

    list = [
        search_admin, search_pim, search_leave, search_time, search_recur,
        search_my, search_perf, search_dash, search_dirc
    ]


# data2
class adminbtn2():
    admin_btn = "Admin"
    usermgn_bt = "//span[normalize-space()='User Management']"
    user_drp = "//ul[@role='menu']//li"
    user_role = "//div[@class='oxd-table-filter-area']//div[2]//div[1]//div[2]//div[1]//div[1]//div[2]//i[1]"
    user_role_lbox = "//div[@role='listbox']"
    status_role = "//div[4]//div[1]//div[2]//div[1]//div[1]//div[2]//i[1]"
    status_role_lbox = "//div[@role='listbox']"
    admindrp = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]'
    essdrp = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]'
    enabled = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]'
    disbled = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[3]'


class pim3:
    pimbtn = "PIM"
    addbtn = "//button[normalize-space()='Add']"
    finput = "//input[@placeholder='First Name']"
    finp_skey = "mohamed"

    minput = "//input[@placeholder='Middle Name']"
    minp_skey = ""

    linput = "//input[@placeholder='Last Name']"
    linp_skey = "hilmas"

    radiobtn = "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    username_input = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    user_skey = "hilmas"

    pwdinput = "//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']"
    pwd_skey = "Admin@123"

    cpwdinput = "//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']"
    pwd_skey = "Admin@123"

    savebtn = "//button[normalize-space()='Save']"

    emplist = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/h6'


class pim4:
    pimbtn = "PIM"
    emp_drp = "//li[@class='oxd-topbar-body-nav-tab --visited']"
    emp_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input'
    emp_name_skey = "5252"
    SAVE = "//button[normalize-space()='Search']"

    editbtn = "//i[@class='oxd-icon bi-pencil-fill']"

    pre_table = "//div[@role='tablist']"


class pim5_personal:
    nickname = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    Nskey = "asm"

    otherid = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    othSkey = "8056"

    Dlisence = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    DlisenSkey = "8056"

    licalbtn = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/i[1]"

    yearbtn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]'

    m_years = "//ul[@role='menu']/li"
    datepicker = "//div[contains(text(),'31')]"

    SSNnumber = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    SINnumber = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    NATdrp_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]'
    NATLBOX = "//div[@role='listbox']/div"
    martial_status = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[1]'
    marit_sts_list = "//div[@role='listbox']/div"

    dob_btn = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]"
    year_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div'
    year_list_btn = "//ul[@role='menu']/li"
    dd_btn = "//div[@class='oxd-calendar-dates-grid']/div"
    ddclose = "//div[@class='oxd-date-input-link --close']"
    male_btn = "//label[normalize-space()='Male']"
    smoker_btn = "//label[normalize-space()='Yes']"
    militry_serv = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/input[1]"

    savebtnl = "Save"


class pim6:

    contact_btn = "//a[normalize-space()='Contact Details']"
    street1 = "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//div[1]//div[1]//div[1]//div[1]//div[2]//input[1]"
    city = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    state = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input'
    pincode = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    mobile = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    save_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'


class pim7:
    EMERcontact = "//a[normalize-space()='Emergency Contacts']"
    add_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    relation = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    homeno = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    mobile = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    wrkmobile = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    save_btn = "//button[normalize-space()='Save']"

    validatECARD = "//div[@class='card-center']/div/div"


class pim8:
    dependents_btn = "//a[normalize-space()='Dependents']"
    Add_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    Name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    relation_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div'
    relation_drp = "//div[@role='listbox']/div"
    Dob_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div'
    Dob_drp = "//div[@class='oxd-calendar-dates-grid']/div"
    save_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'


class pim9:
    job_btn = "//a[normalize-space()='Job']"
    jDate_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div'
    jDate_drp = "//div[@class='oxd-calendar-dates-grid']/div"
    jTitle_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div'
    jTitle_drp = "//div[@role='listbox']//div"
    Jspecfic = "//div[@class='input-container --disabled']"
    Jcatago_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div'
    Jcata_drp = "//div[@role='listbox']/div"

    radio_Btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label/span'
    ConT_sDate = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
    ConT_Edate = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]"
    Save_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button'


class pim1011:
    job_btn = "//a[normalize-space()='Job']"
    Emp_termi_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'
    Ter_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div'
    ter_drp = "//div[@class='oxd-calendar-dates-grid']/div"
    Ter_res_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div'
    Ter_res_drp = "//div[@role='listbox']//div"
    save = "//div[@role='document']//button[@type='submit'][normalize-space()='Save']"
    act_emp = "//button[normalize-space()='Activate Employment']"
    act_date = "//p[@class='oxd-text oxd-text--p orangehrm-terminate-date']"
