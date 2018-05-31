from django.db import models

# Create your models here.
from health.models import Counties, SubCounty


class Approved_Degree_Diploma_Programs(models.Model):
    approved_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    approved_degree_programmes = models.IntegerField()
    approved_private_university_degreeprogrammes = models.IntegerField()
    validated_diploma_programmes = models.IntegerField()



class NationalTrendsKcseCandidatesMeanGradebySex(models.Model):
    national_trends_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    a_plain = models.CharField(max_length=100)
    a_minus = models.CharField(max_length=100)
    b_plus = models.CharField(max_length=100)
    b_plain = models.CharField(max_length=100)
    b_minus = models.CharField(max_length=100)
    c_plus = models.CharField(max_length=100)
    c_plain = models.CharField(max_length=100)
    c_minus = models.CharField(max_length=100)
    d_plus = models.CharField(max_length=100)
    d_plain = models.CharField(max_length=100)
    d_minus = models.CharField(max_length=100)
    e_plain = models.CharField(max_length=100)

class Number_Educational_Institutions(models.Model):
    educational_institutions_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=100)
    schools_primary_secondary = models.CharField(max_length=100)
    teacher_training_colleges  = models.CharField(max_length=100)
    tivet_institutions  = models.CharField(max_length=100)
    universities  = models.CharField(max_length=100)

class StudentEnrollmentBySexTechnicalInstitutions(models.Model):
    student_enrollment_id = models.AutoField(primary_key=True)
    institution = models.CharField(max_length=100)
    year = models.IntegerField()
    male = models.IntegerField()
    female = models.IntegerField()

class StudentEnrollmentPublicUniversities(models.Model):
    student_enrollment_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    undergraduates = models.IntegerField()
    postgraduates = models.IntegerField()
    other = models.IntegerField()

class TotalSecondarySchoolEnrollmentByYear(models.Model):
    school_enrollment_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=100)
    county = models.ForeignKey(Counties)
    number_of_students = models.CharField(max_length=100)

class EnrollmentSecondarySchoolsByLevelAndSex(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    boys = models.CharField(max_length=100)
    girls = models.CharField(max_length=100)

############################################CSA############################################
class Csa_AdultEducationCentresBySubCounty(models.Model):
    adult_centre_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    sub_county_id = models.IntegerField()
    centres = models.CharField(max_length=100)
    year = models.IntegerField()

class Csa_AdultEducationEnrolmentBySexAndSubcounty(models.Model):
    adult_enrolment_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    sub_county_id = models.IntegerField()
    number = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

class Csa_AdultEducationProficiencyTestResults(models.Model):
    adult_proficiency_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    sub_county_id = models.IntegerField()
    no_sat = models.IntegerField()
    no_passed = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

class Csa_EcdeCentresByCategoryAndSubCounty(models.Model):
    ecde_centre_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    sub_county_id = models.IntegerField()
    no_of_centres = models.IntegerField()
    category = models.CharField(max_length=100)
    year = models.IntegerField()

class Csa_PrimaryEnrolmentAndAccessIndicators(models.Model):
    primary_enrolment_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    enrolment = models.IntegerField()
    ger = models.FloatField()
    ner = models.FloatField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

class Csa_PrimarySchoolEnrollmentByClassSexAndSubCounty(models.Model):
    primary_enrollment_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    sub_county_id = models.IntegerField()
    class_1 = models.IntegerField()
    class_2 = models.IntegerField()
    class_3 = models.IntegerField()
    class_4 = models.IntegerField()
    class_5 = models.IntegerField()
    class_6 = models.IntegerField()
    class_7 = models.IntegerField()
    class_8 = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

class Csa_PrimarySchoolsByCategoryAndSubCounty(models.Model):
    primary_schools_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    sub_county_id = models.IntegerField()
    no_of_schools = models.IntegerField()
    category = models.CharField(max_length=100)
    year = models.IntegerField()

class Csa_SecondaryEnrolmentAndAccessIndicators(models.Model):
    secondary_enrolment_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    enrolment = models.IntegerField()
    ger = models.FloatField()
    ner = models.FloatField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

class Csa_SecondarySchoolEnrollmentByClassSexSubCounty(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    sub_county_id = models.IntegerField()
    form_1 = models.IntegerField()
    form_2 = models.IntegerField()
    form_3 = models.IntegerField()
    form_4 = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

class Csa_SecondarySchoolsByCategoryAndSubCounty(models.Model):
    sec_schools_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    sub_county_id = models.IntegerField()
    no_of_schools = models.IntegerField()
    category = models.CharField(max_length=100)
    year = models.IntegerField()

class Csa_StudentEnrolmentInYouthPolytechnics(models.Model):
    youth_poly_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    sub_county_id = models.IntegerField()
    institution_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    male = models.IntegerField()
    female = models.IntegerField()
    year = models.IntegerField()

class Csa_TeacherTrainingColleges(models.Model):
    teacher_colleges_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    category = models.CharField(max_length=100)
    pre_primary = models.IntegerField()
    primary_sc = models.IntegerField()
    secondary = models.IntegerField()
    year = models.IntegerField()

class Csa_YouthPolytechnicsByCategoryAndSubCounty(models.Model):
    youth_poly_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    sub_county_id = models.IntegerField()
    public = models.IntegerField()
    private = models.IntegerField()
    year = models.IntegerField()

############################################Economic Survey############################################
class Es_Educational_Institutions_Public_Tivet(models.Model):
    institution_id = models.AutoField(primary_key=True)
    institution = models.CharField(max_length=100)
    number = models.IntegerField()
    year = models.IntegerField()

class Es_Educational_Institutions_Schools(models.Model):
    institution_id = models.AutoField(primary_key=True)
    institution = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    number = models.IntegerField()
    year = models.IntegerField()

class Es_KcpeCandidatesAndMeanSubjectScore_Candidates(models.Model):
    candidates_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=100)
    number = models.IntegerField()
    year = models.IntegerField()

class Es_KcpeCandidatesAndMeanSubjectScore_Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    mean_score = models.DecimalField(max_digits=20, decimal_places=2)
    year = models.IntegerField()

class Es_NationalGovtDevelopmentAndRecurrentExpenditure(models.Model):
    expenditure_id = models.AutoField(primary_key=True)
    expenditure = models.CharField(max_length=100)
    expenditure_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    year = models.IntegerField()

class Es_PrivateCandidatesRegisteredForKcpeBySex(models.Model):
    kcpe_candidates_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    proficiency = models.IntegerField()
    kcpe = models.IntegerField()
    gender = models.CharField(max_length=100)

class Es_Public_Secondary_School_Trained_Teachers(models.Model):
    teachers_id = models.AutoField(primary_key=True)
    teachers = models.CharField(max_length=100)
    number = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

class Es_Public_Secondary_School_Untrained_Teachers(models.Model):
    teachers_id = models.AutoField(primary_key=True)
    teachers = models.CharField(max_length=100)
    number = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

class Es_Teacher_Trainees_Diploma_Enrolment(models.Model):
    diploma_enrolment_id = models.AutoField(primary_key=True)
    diploma_year = models.CharField(max_length=100)
    number = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

class Es_Teacher_Trainees_Private_Enrolment(models.Model):
    private_enrolment_id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

class Es_Teacher_Trainees_Public_Enrolment(models.Model):
    public_enrolment_id = models.AutoField(primary_key=True)
    primary_year = models.CharField(max_length=100)
    number = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

############################################Edstat############################################

class Edstat_Ecde_Enrollment_And_Enrollment_Rates_By_County(models.Model):
    ecde_enrollment_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    ecde_enrollment = models.IntegerField()
    gross_enrollment_rate = models.DecimalField(decimal_places=2, max_digits=10)
    net_enrollment_rate = models.DecimalField(decimal_places=2, max_digits=10)
    gender = models.CharField(max_length=100)
    year = models.CharField(max_length=10)

class Edstat_Kcpe_Examination_Candidature(models.Model):
    candidature_id = models.AutoField(primary_key=True)
    kcpe_candidature = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.CharField(max_length=10)

class Edstat_Kcpe_Examination_Results_By_Subject(models.Model):
    kcpe_result_id = models.AutoField(primary_key=True)
    kcpe_result = models.DecimalField(decimal_places=2, max_digits=10)
    subject = models.CharField(max_length=100)
    year = models.CharField(max_length=10)

class Edstat_Kcse_Examination_Results(models.Model):
    kcse_result_id = models.AutoField(primary_key=True)
    number_of_candidates = models.IntegerField()
    kcse_grade = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    year = models.CharField(max_length=10)

class Edstat_Primary_Enrollment_Enrollment_Rates_County(models.Model):
    primary_enrollment_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    primary_enrollment = models.IntegerField()
    gross_enrollment_rate = models.DecimalField(decimal_places=2, max_digits=10)
    net_enrollment_rate = models.DecimalField(decimal_places=2, max_digits=10)
    gender = models.CharField(max_length=100)
    year = models.CharField(max_length=10)

class Edstat_Secondary_Enrollment_Enrollment_Rates_County(models.Model):
    secondary_enrollment_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    secondary_enrollment = models.IntegerField()
    gross_enrollment_rate = models.DecimalField(decimal_places=2, max_digits=10)
    net_enrollment_rate = models.DecimalField(decimal_places=2, max_digits=10)
    gender = models.CharField(max_length=100)
    year = models.CharField(max_length=10)

############################################Gender Fact Sheet############################################
class Number_Of_Candidates_By_Sex_In_Kcse(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    number = models.IntegerField()
    proportion = models.DecimalField(max_digits=10, decimal_places=1)
    gender = models.CharField(max_length=10)

class primary_school_enrolments_by_sex (models.Model):
    enrolment_id = models.AutoField (primary_key=True)
    year = models.IntegerField()
    boys = models.IntegerField()
    girls = models.IntegerField()
    total = models.IntegerField()
    percentage_girls = models.DecimalField(max_digits=10, decimal_places=1)
    parity_index = models.DecimalField(max_digits=10, decimal_places=1)

class Public_Primary_School_Teachers_By_Sex(models.Model):
    candidate_id = models.AutoField (primary_key=True)
    year = models.IntegerField()
    number = models.IntegerField()
    proportion = models.DecimalField(max_digits=10, decimal_places=1)
    gender = models.CharField(max_length=10)

class Public_Primaryteachers_TrainingCollege_Enrolment(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    number = models.IntegerField()
    proportion = models.DecimalField(max_digits=10, decimal_places=1)
    gender = models.CharField(max_length=10)

class Public_Secondary_School_Teachers_By_Sex(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    number = models.IntegerField()
    proportion = models.DecimalField(max_digits=10, decimal_places=1)
    gender = models.CharField(max_length=10)

class Secondary_School_Enrolment_By_Sex (models.Model):
    enrolment_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    boys = models.IntegerField()
    girls = models.IntegerField()
    total = models.IntegerField()
    percentage_girls = models.DecimalField(max_digits=10, decimal_places=1)
    parity_index = models.DecimalField(max_digits=10, decimal_places=1)


############################################KIHBIS II ############################################

class Population_Distribution_Above_Three_School_Attendance(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county_id = models.IntegerField()
    currently_attending = models.DecimalField(max_digits=10, decimal_places=1)
    not_attending = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()


class Distribution_AboveThreeYears_Training (models. Model):
    distribution_id = models.AutoField(primary_key=True)
    county_id = models.IntegerField()
    ever_attended = models.DecimalField(max_digits=10, decimal_places=1)
    never_attended = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()

class Distribution_AboveThreeYears_Highestlevel_Reached (models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county_id = models.IntegerField()
    pre_primary = models.DecimalField(max_digits=10, decimal_places=1)
    primary = models.DecimalField(max_digits=10, decimal_places=1)
    post_primary = models.DecimalField(max_digits=10, decimal_places=1)
    secondary = models.DecimalField(max_digits=10, decimal_places=1)
    college = models.DecimalField(max_digits=10, decimal_places=1)
    university = models.DecimalField(max_digits=10, decimal_places=1)
    madrassa_duksi = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()


class Distribution_SixThirteen_By_SchoolType(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county_id = models.IntegerField()
    day = models.DecimalField(max_digits=10, decimal_places=1)
    boarding = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    type = models.CharField(max_length=10)

class Distribution_AboveFifteen_Ability_ReadWrite(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county_id = models.IntegerField()
    literate = models.DecimalField(max_digits=10, decimal_places=1)
    illiterate = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()
    gender = models.CharField(max_length=10)

class Distribution_Three_Twentyfour_SchoolAttendance(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county_id = models.IntegerField()
    currently_attending = models.DecimalField(max_digits=10, decimal_places=1)
    not_attending = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()
    age_group = models.CharField(max_length=10)

class Gross_Attendance_Ratio_By_Level(models.Model):
    ratio_id = models.AutoField(primary_key=True)
    county_id = models.IntegerField()
    pre_primary = models.DecimalField(max_digits=10, decimal_places=1)
    primary = models.DecimalField(max_digits=10, decimal_places=1)
    secondary = models.DecimalField(max_digits=10, decimal_places=1)
    gender = models.CharField(max_length=10)

class Net_Attendance_Ratio_By_Level(models.Model):
    ratio_id = models.AutoField(primary_key=True)
    county_id = models.IntegerField()
    pre_primary = models.DecimalField(max_digits=10, decimal_places=1)
    primary = models.DecimalField(max_digits=10, decimal_places=1)
    secondary = models.DecimalField(max_digits=10, decimal_places=1)
    gender = models.CharField(max_length=10)

class Distribution_Highest_Education_Qualification(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county_id   = models.IntegerField()
    none = models.DecimalField(max_digits=10, decimal_places=1)
    cpe_kcpe = models.DecimalField(max_digits=10, decimal_places=1)
    kape = models.DecimalField(max_digits=10, decimal_places=1)
    kjse = models.DecimalField(max_digits=10, decimal_places=1)
    kce_kcse = models.DecimalField(max_digits=10, decimal_places=1)
    kace_eaace = models.DecimalField(max_digits=10, decimal_places=1)
    certificate = models.DecimalField(max_digits=10, decimal_places=1)
    diploma = models.DecimalField(max_digits=10, decimal_places=1)
    degree = models.DecimalField(max_digits=10, decimal_places=1)
    post_literacy_cert = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals  = models.IntegerField()









