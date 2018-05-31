from django.shortcuts import render

# Create your views here.

# def education(request):
#     return render(request, template_name="knbs_bi/education.html")
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from education.models import Approved_Degree_Diploma_Programs, \
    NationalTrendsKcseCandidatesMeanGradebySex, Number_Educational_Institutions, \
    StudentEnrollmentBySexTechnicalInstitutions, StudentEnrollmentPublicUniversities, \
    TotalSecondarySchoolEnrollmentByYear, Csa_AdultEducationCentresBySubCounty, \
    Csa_AdultEducationEnrolmentBySexAndSubcounty, Csa_AdultEducationProficiencyTestResults, \
    Csa_EcdeCentresByCategoryAndSubCounty, Csa_PrimaryEnrolmentAndAccessIndicators, \
    Csa_PrimarySchoolEnrollmentByClassSexAndSubCounty, Csa_PrimarySchoolsByCategoryAndSubCounty, \
    Csa_SecondaryEnrolmentAndAccessIndicators, Csa_SecondarySchoolEnrollmentByClassSexSubCounty, \
    Csa_SecondarySchoolsByCategoryAndSubCounty, Csa_StudentEnrolmentInYouthPolytechnics, Csa_TeacherTrainingColleges, \
    Csa_YouthPolytechnicsByCategoryAndSubCounty, Edstat_Ecde_Enrollment_And_Enrollment_Rates_By_County, \
    Edstat_Primary_Enrollment_Enrollment_Rates_County, Edstat_Secondary_Enrollment_Enrollment_Rates_County, \
    Edstat_Kcpe_Examination_Candidature, Edstat_Kcpe_Examination_Results_By_Subject, Edstat_Kcse_Examination_Results
from health.models import Counties, SubCounty, Sectors


def education(request):
    return render(request, template_name='knbs_bi/education.html')

def no_records(request):
    datasets = Sectors.objects.order_by('Education')
    data_count = Sectors.objects.count()
    context = {'edu_count': data_count}
    return render(request, 'knbs_bi/index.html', context)
##########################################################################################################################


############################################Approved Degree and Diploma Programmes############################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def diplomaDegree(request):
    dip_degree = Approved_Degree_Diploma_Programs.objects.all()

    dip_deg = []

    if dip_degree:
        for level in dip_degree:
            c = {'year': level.year, 'approved_degree_programmes': level.approved_degree_programmes,
                 'approved_private_university_degree_programmes': level.approved_private_university_degreeprogrammes,
                 'validated_diploma_programmes': level.validated_diploma_programmes}
            dip_deg.append(c)
    else:
        pass
    return Response(dip_deg)

#Launch Page
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def diplomaDegreeView(request):
    dip_degree = Approved_Degree_Diploma_Programs.objects.all()

    dip_deg = []

    if dip_degree:
        for level in dip_degree:
            c = {'id':level.approved_id, 'year': level.year, 'approved_degree_programmes': level.approved_degree_programmes,
                 'approved_private_university_degree_programmes': level.approved_private_university_degreeprogrammes,
                 'validated_diploma_programmes': level.validated_diploma_programmes}
            dip_deg.append(c)
            context = {'programs': dip_deg}
    else:
        pass
    return render(request, 'knbs_bi/education_approved_degree_and_validated_diploma_programs.html', context)

# Add View
def addDiplomaDegreeView(request):
    return render(request, 'knbs_bi/education_approved_degree_and_validated_diploma_programs_add.html')

# Edit View
def editDiplomaDegreeView(request):
    return render(request, 'knbs_bi/education_approved_degree_and_validated_diploma_programs_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addDiplomaDegree(request):
    program_add = Approved_Degree_Diploma_Programs(year=request.data['year'], approved_degree_programmes=request.data['degree'],
                                                    approved_private_university_degreeprogrammes=request.data['private_degree'],
                                                    validated_diploma_programmes=request.data['diploma'])
    if program_add:
        program_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))

def editDiplomaDegree(request):
    program_edit = Approved_Degree_Diploma_Programs.objects.get(approved_id=request.data['approved_id'])

    if 'year' in request.data:
        program_edit.year = request.data['year']
    if 'degree' in request.data:
        program_edit.approved_degree_programmes = request.data['degree']
    if 'private_degree' in request.data:
        program_edit.approved_private_university_degreeprogrammes = request.data['private_degree']
    if 'diploma' in request.data:
        program_edit.validated_diploma_programmes = request.data['diploma']


    program_edit.save()
    return Response(status=status.HTTP_201_CREATED)

##########################################################################################################################

# @api_view(http_method_names=['GET'])
# @renderer_classes((JSONRenderer,))
# def secondaryLevelSex(request):
#     sec_level_sex = EnrollmentSecondarySchoolsByLevelAndSex.objects.all()
#
#     enrollments = []
#
#     if sec_level_sex:
#         for enrollment in sec_level_sex:
#             c = {'year': enrollment.year, 'level': enrollment.level, 'no_of_boys': enrollment.boys,
#                  'no_of_girls': enrollment.girls}
#             enrollments.append(c)
#     else:
#         pass
#     return Response(enrollments)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def trendsKcse(request):
    national_trends = NationalTrendsKcseCandidatesMeanGradebySex.objects.all()

    trends = []

    if national_trends:
        for trend in national_trends:
            c = {'gender': trend.gender, 'year': trend.year, 'no_A_Plain': trend.a_plain, 'no_A-': trend.a_minus,
                 'no_B+': trend.b_plus, 'no_B_Plain': trend.b_plain, 'no_B-': trend.b_minus,
                 'no_C+':trend.c_plus, 'no_C_Plain': trend.c_plain, 'no_C-': trend.c_minus,
                 'no_D+': trend.d_plus, 'no_D': trend.d_plain, 'no_D-': trend.d_minus,
                 'no_E': trend.e_plain}
            trends.append(c)
    else:
        pass
    return Response(trends)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def numInstitutions(request):
    num_institutions = Number_Educational_Institutions.objects.all()

    institutions = []

    if num_institutions:
        for institution in num_institutions:
            c = {'year': institution.year, 'no_of_primary_secondary_schools': institution.schools_primary_secondary,
                 'no_of_teacher_training_colleges': institution.teacher_training_colleges,
                 'no_of_tivet_institutions':institution.tivet_institutions, 'no_of_universities': institution.universities}
            institutions.append(c)
    else:
        pass
    return Response(institutions)

############################################Student Enrolment by Sex in Technical Institutions############################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def studentEnrollment(request):
    stu_enrollment = StudentEnrollmentBySexTechnicalInstitutions.objects.all()

    enrollments = []

    if stu_enrollment:
        for enrollment in stu_enrollment:
            c = {'institution': enrollment.institution, 'year': enrollment.year, 'no_of_male': enrollment.male,
                 'no_of_female': enrollment.female}
            enrollments.append(c)
    else:
        pass
    return Response(enrollments)

#Launch Page
def studentEnrollmentView(request):
    stu_enrollment = StudentEnrollmentBySexTechnicalInstitutions.objects.all()

    enrollments = []

    if stu_enrollment:
        for enrollment in stu_enrollment:
            c = {'id': enrollment.student_enrollment_id, 'institution': enrollment.institution, 'year': enrollment.year, 'no_of_male': enrollment.male,
                 'no_of_female': enrollment.female}
            enrollments.append(c)
            context = {'enrollments': enrollments}
    else:
        pass
    return render(request, 'knbs_bi/education_student_enrollment_by_sex_technical_institutions.html', context)

# Add View
def addStudentEnrollmentView(request):
    return render(request, 'knbs_bi/education_student_enrollment_by_sex_technical_institutions_add.html')

# Edit View
def editStudentEnrollmentView(request):
    return render(request, 'knbs_bi/education_student_enrollment_by_sex_technical_institutions_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addStudentEnrollment(request):
    student_add = StudentEnrollmentBySexTechnicalInstitutions(institution=request.data['institution'], year=request.data['year'],
                                                    male=request.data['male'],
                                                    female=request.data['female'])
    if student_add:
        student_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editStudentEnrollment(request):
    student_edit = StudentEnrollmentBySexTechnicalInstitutions.objects.get(student_enrollment_id=request.data['enrollment_id'])

    if 'institution' in request.data:
        student_edit.institution = request.data['institution']
    if 'year' in request.data:
        student_edit.year = request.data['year']
    if 'male' in request.data:
        student_edit.male = request.data['male']
    if 'female' in request.data:
        student_edit.female = request.data['female']


    student_edit.save()
    return Response(status=status.HTTP_201_CREATED)



############################################Student Enrolment in Public Universities############################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def studentEnrollmentPublic(request):
    stu_enrollment_public = StudentEnrollmentPublicUniversities.objects.all()

    stu_enrollment = []

    if stu_enrollment_public:
        for enrollment in stu_enrollment_public:
            c = {'year': enrollment.year, 'no_of_undergraduates': enrollment.undergraduates,
                 'no_of_postgraduates': enrollment.postgraduates, 'other': enrollment.other}
            stu_enrollment.append(c)
    else:
        pass
    return Response(stu_enrollment)

#Launch Page
def studentEnrollmentPublicView(request):
    stu_enrollment_public = StudentEnrollmentPublicUniversities.objects.all()

    stu_enrollment = []

    if stu_enrollment_public:
        for enrollment in stu_enrollment_public:
            c = {'id':enrollment.student_enrollment_id, 'year': enrollment.year, 'no_of_undergraduates': enrollment.undergraduates,
                 'no_of_postgraduates': enrollment.postgraduates, 'other': enrollment.other}
            stu_enrollment.append(c)
            context = {'enrollments': stu_enrollment}
    else:
        pass
    return render(request, 'knbs_bi/education_student_enrollment_public_universities.html', context)

# Add View
def addStudentEnrollmentPublicView(request):
    return render(request, 'knbs_bi/education_student_enrollment_public_universities_add.html')

# Edit View
def editStudentEnrollmentPublicView(request):
    return render(request, 'knbs_bi/education_student_enrollment_public_universities_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addStudentEnrollmentPublic(request):
    student_add = StudentEnrollmentPublicUniversities(year=request.data['year'], undergraduates=request.data['undergraduates'],
                                                    postgraduates=request.data['postgraduates'],
                                                    other=request.data['other'])
    if student_add:
        student_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editStudentEnrollmentPublic(request):
    student_edit = StudentEnrollmentPublicUniversities.objects.get(student_enrollment_id=request.data['enrollment_id'])

    if 'year' in request.data:
        student_edit.year = request.data['year']
    if 'undergraduates' in request.data:
        student_edit.undergraduates = request.data['undergraduates']
    if 'postgraduates' in request.data:
        student_edit.postgraduates = request.data['postgraduates']
    if 'other' in request.data:
        student_edit.other = request.data['other']


    student_edit.save()
    return Response(status=status.HTTP_201_CREATED)

############################################Total Secondary School Enrollment############################################
#Launch Page
def viewSecSchoolEnrollment(request):
    sec_school_enrol = TotalSecondarySchoolEnrollmentByYear.objects.all()

    totals = []

    if sec_school_enrol:
        for total in sec_school_enrol:
            county = Counties.objects.get(county_id=total.county_id)
            c = {'enrollment_id': total.school_enrollment_id, 'year': total.year, 'county': county.county_name,
                 'students': total.number_of_students}
            totals.append(c)
            context = {'totals': totals}
    return render(request, 'knbs_bi/education_total_secondary_school_enrollment_by_year_data.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def secSchoolEnrollment(request):
    sec_school_enrol = TotalSecondarySchoolEnrollmentByYear.objects.all()

    totals = []

    if sec_school_enrol:
        for total in sec_school_enrol:
            county = Counties.objects.get(county_id=total.county_id)
            c = {'year': total.year, 'county': county.county_name, 'number_of_students': total.number_of_students}
            totals.append(c)
    else:
        pass
    return Response(totals)

#Add School Enrollment
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addSchoolEnrollment(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        sec_add = TotalSecondarySchoolEnrollmentByYear(year=request.data['year'], county_id=kaunti,
                                                       number_of_students=request.data['students'])
        if sec_add:
            sec_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit School Enrollment
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editSchoolEnrollment(request):
    sec_update = TotalSecondarySchoolEnrollmentByYear.objects.get(school_enrollment_id=request.data['enrol_id'])

    if 'year' in request.data:
        sec_update.year = request.data['year']
    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            sec_update.county_id = counties.county_id
    if 'students' in request.data:
            sec_update.number_of_students = request.data['students']

    sec_update.save()
    return Response(status=status.HTTP_201_CREATED)


#Secondary Enrollment Add View
def addSecSchoolEnrollment(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    # translation.activate('en')
    return render(request, 'knbs_bi/education_total_secondary_school_enrollment_by_year_data_add.html', context)

#Secondary Enrollment Edit View
def editSecSchoolEnrollment(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/education_total_secondary_school_enrollment_by_year_data_edit.html', context)

############################################CSA############################################

####################################Primary School Enrolment by Class, Sex and SubCounty####################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def primaryEnrollmentSexCounty(request):
    pri_enrol = Csa_PrimarySchoolEnrollmentByClassSexAndSubCounty.objects.all()

    enrollments = []

    if pri_enrol:
        for enrollment in pri_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=enrollment.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'county': county.county_name, 'sub_county': sc.subcounty_name, 'class_1': enrollment.class_1,
                         'class_2': enrollment.class_2, 'class_3': enrollment.class_3, 'class_4': enrollment.class_4,
                         'class_5': enrollment.class_5, 'class_6': enrollment.class_6, 'class_7': enrollment.class_7,
                         'class_8': enrollment.class_8, 'gender': enrollment.gender, 'year': enrollment.year}
                    enrollments.append(c)
    else:
        pass

    return Response(enrollments)

#launch Page
def primaryEnrollmentSexCountyView(request):
    pri_enrol = Csa_PrimarySchoolEnrollmentByClassSexAndSubCounty.objects.all()

    enrollments = []

    if pri_enrol:
        for enrollment in pri_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=enrollment.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'id': enrollment.primary_enrollment_id, 'county': county.county_name, 'sub_county': sc.subcounty_name, 'class_1': enrollment.class_1,
                         'class_2': enrollment.class_2, 'class_3': enrollment.class_3, 'class_4': enrollment.class_4,
                         'class_5': enrollment.class_5, 'class_6': enrollment.class_6, 'class_7': enrollment.class_7,
                         'class_8': enrollment.class_8, 'gender': enrollment.gender, 'year': enrollment.year}
                    enrollments.append(c)
                    context = {'enrollments': enrollments}
    else:
        pass

    return render(request, 'knbs_bi/education_csa_primary_school_enrollment_by_class_sex_and_subcounty.html', context)

# Add View
def addPrimaryEnrollmentSexCountyView(request):
    all_counties = Counties.objects.all()
    subcounty = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': subcounty}
    return render(request, 'knbs_bi/education_csa_primary_school_enrollment_by_class_sex_and_subcounty_add.html', context)

# Edit View
def editPrimaryEnrollmentSexCountyView(request):
    all_counties = Counties.objects.all()
    subcounty = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': subcounty}
    return render(request, 'knbs_bi/education_csa_primary_school_enrollment_by_class_sex_and_subcounty_edit.html', context)

# View More
def morePrimaryEnrollmentSexCounty(request):
    return render(request, template_name='knbs_bi/education_csa_primary_school_enrollment_by_class_sex_and_subcounty_view.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addPrimaryEnrollmentSexCounty(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])

    if counties and sub:
        kaunti = counties.county_id
        sub_kaunti = sub.subcounty_id

        primary_add = Csa_PrimarySchoolEnrollmentByClassSexAndSubCounty(county_id=kaunti, sub_county_id=sub_kaunti, class_1=request.data['class_one'],
                                                               class_2=request.data['class_two'], class_3=request.data['class_three'], class_4=request.data['class_four'],
                                                               class_5=request.data['class_five'], class_6=request.data['class_six'], class_7=request.data['class_seven'],
                                                               class_8=request.data['class_eight'], gender=request.data['gender'], year=request.data['year'])
        if primary_add:
            primary_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editPrimaryEnrollmentSexCounty(request):
    primary_edit = Csa_PrimarySchoolEnrollmentByClassSexAndSubCounty.objects.get(primary_enrollment_id=request.data['primary_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            primary_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            primary_edit.sub_county_id = sub.subcounty_id

    if 'class_one' in request.data:
        primary_edit.class_1 = request.data['class_one']
    if 'class_two' in request.data:
        primary_edit.class_2 = request.data['class_two']
    if 'class_three' in request.data:
        primary_edit.class_3 = request.data['class_three']
    if 'class_four' in request.data:
        primary_edit.class_4 = request.data['class_four']
    if 'class_five' in request.data:
        primary_edit.class_5 = request.data['class_five']
    if 'class_six' in request.data:
        primary_edit.class_6 = request.data['class_six']
    if 'class_seven' in request.data:
        primary_edit.class_7 = request.data['class_seven']
    if 'class_eight' in request.data:
        primary_edit.class_8 = request.data['class_eight']
    if 'gender' in request.data:
        primary_edit.gender = request.data['gender']
    if 'year' in request.data:
        primary_edit.year = request.data['year']

    primary_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


####################################Secondary Enrolment by Sex and SubCounty####################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def secondaryEnrollmentSexCounty(request):
    sec_enrol = Csa_SecondarySchoolEnrollmentByClassSexSubCounty.objects.all()

    enrollments = []

    if sec_enrol:
        for enrollment in sec_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=enrollment.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'county': county.county_name, 'sub_county': sc.subcounty_name, 'form_1': enrollment.form_1,
                         'form_2': enrollment.form_2, 'form_3': enrollment.form_3, 'form_4': enrollment.form_4,
                         'gender': enrollment.gender, 'year': enrollment.year}
                    enrollments.append(c)
    else:
        pass

    return Response(enrollments)

#Launch Page
def secondaryEnrollmentSexCountyView(request):
    sec_enrol = Csa_SecondarySchoolEnrollmentByClassSexSubCounty.objects.all()

    enrollments = []

    if sec_enrol:
        for enrollment in sec_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=enrollment.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'id':enrollment.enrollment_id,'county': county.county_name, 'sub_county': sc.subcounty_name, 'form_1': enrollment.form_1,
                         'form_2': enrollment.form_2, 'form_3': enrollment.form_3, 'form_4': enrollment.form_4,
                         'gender': enrollment.gender, 'year': enrollment.year}
                    enrollments.append(c)
                    context = {'enrollments': enrollments}
    else:
        pass

    return render(request,'knbs_bi/education_csa_secondaryschoolenrollmentbyclasssexsubcounty.html', context)

# Add View
def addSecondaryEnrollmentSexCountyView(request):
    all_counties = Counties.objects.all()
    subcounty = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': subcounty}
    return render(request, 'knbs_bi/education_csa_secondaryschoolenrollmentbyclasssexsubcounty_add.html', context)

# Edit View
def editSecondaryEnrollmentSexCountyView(request):
    all_counties = Counties.objects.all()
    subcounty = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': subcounty}
    return render(request, 'knbs_bi/education_csa_secondaryschoolenrollmentbyclasssexsubcounty_edit.html', context)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addSecondaryEnrollmentSexCounty(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])

    if counties and sub:
        kaunti = counties.county_id
        sub_kaunti = sub.subcounty_id

        enrollment_add = Csa_SecondarySchoolEnrollmentByClassSexSubCounty(county_id=kaunti, sub_county_id=sub_kaunti, form_1=request.data['form_one'],
                                                               form_2=request.data['form_two'], form_3=request.data['form_three'], form_4=request.data['form_four'],
                                                               gender=request.data['gender'], year=request.data['year'])
        if enrollment_add:
            enrollment_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editSecondaryEnrollmentSexCounty(request):
    enrollment_edit = Csa_SecondarySchoolEnrollmentByClassSexSubCounty.objects.get(enrollment_id=request.data['enrollment_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            enrollment_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            enrollment_edit.sub_county_id = sub.subcounty_id

    if 'form_one' in request.data:
        enrollment_edit.form_1 = request.data['form_one']
    if 'form_two' in request.data:
        enrollment_edit.form_2 = request.data['form_two']
    if 'form_three' in request.data:
        enrollment_edit.form_3 = request.data['form_three']
    if 'form_four' in request.data:
        enrollment_edit.form_4 = request.data['form_four']
    if 'gender' in request.data:
        enrollment_edit.gender = request.data['gender']
    if 'year' in request.data:
        enrollment_edit.year = request.data['year']

    enrollment_edit.save()
    return Response(status=status.HTTP_201_CREATED)
####################################Secondary Schools by Category and SubCounty##################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def secondaryCategorySubCounty(request):
    sec_cat = Csa_SecondarySchoolsByCategoryAndSubCounty.objects.all()

    secondaries = []

    if sec_cat:
        for secondary in sec_cat:
            county = Counties.objects.get(county_id=secondary.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=secondary.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'county': county.county_name, 'sub_county': sc.subcounty_name, 'public': secondary.public,
                         'private': secondary.private, 'year': secondary.year}
                    secondaries.append(c)
    else:
        pass

    return Response(secondaries)



####################################Youth Polytechnics by Category and SubCounty####################################
def polytechnicCategorySubcountyView(request):
    poly_cat = Csa_YouthPolytechnicsByCategoryAndSubCounty.objects.all()

    polytechnics = []

    if poly_cat:
        for polytechnic in poly_cat:
            county = Counties.objects.get(county_id=polytechnic.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=polytechnic.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'id': polytechnic.youth_poly_id, 'county': county.county_name, 'sub_county': sc.subcounty_name, 'public': polytechnic.public,
                         'private': polytechnic.private, 'year': polytechnic.year}
                    polytechnics.append(c)
                    context = {'polytechnics': polytechnics}
    else:
        pass

    return render(request, 'knbs_bi/education_csa_youth_polytechnics_by_category_and_subcounty.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def polytechnicCategorySubcounty(request):
    poly_cat = Csa_YouthPolytechnicsByCategoryAndSubCounty.objects.all()

    polytechnics = []

    if poly_cat:
        for polytechnic in poly_cat:
            county = Counties.objects.get(county_id=polytechnic.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=polytechnic.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'county': county.county_name, 'sub_county': sc.subcounty_name, 'public': polytechnic.public,
                         'private': polytechnic.private, 'year': polytechnic.year}
                    polytechnics.append(c)
    else:
        pass

    return Response(polytechnics)

# Add View
def addPolytechnicCategorySubcountyView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/education_csa_youth_polytechnics_by_category_and_subcounty_add.html', context)

# Edit View
def editPolytechnicCategorySubcountyView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/education_csa_youth_polytechnics_by_category_and_subcounty_edit.html', context)


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addPolytechnicCategorySubcounty(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])

    if counties and sub:
        kaunti = counties.county_id
        sub_kaunti = sub.subcounty_id

        poly_cat_add = Csa_YouthPolytechnicsByCategoryAndSubCounty(county_id=kaunti, sub_county_id=sub_kaunti, public=request.data['public'],
                                                               private=request.data['private'], year=request.data['year'])
        if poly_cat_add:
            poly_cat_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editPolytechnicCategorySubcounty(request):
    poly_cat_edit = Csa_YouthPolytechnicsByCategoryAndSubCounty.objects.get(youth_poly_id=request.data['poly_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            poly_cat_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            poly_cat_edit.sub_county_id = sub.subcounty_id

    if 'public' in request.data:
        poly_cat_edit.public = request.data['public']
    if 'private' in request.data:
        poly_cat_edit.private = request.data['private']
    if 'year' in request.data:
        poly_cat_edit.year = request.data['year']

    poly_cat_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

####################################Primary Category Subcouny####################################
#Launch Page
def primaryCategorySubCountyView(request):
    pri_cat = Csa_PrimarySchoolsByCategoryAndSubCounty.objects.all()

    primaries = []

    if pri_cat:
        for primary in pri_cat:
            county = Counties.objects.get(county_id=primary.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=primary.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'id': primary.primary_schools_id, 'county': county.county_name, 'sub_county': sc.subcounty_name, 'schools': primary.no_of_schools,
                         'category': primary.category, 'year': primary.year}
                    primaries.append(c)
                    context = {'primaries': primaries}
    else:
        pass

    return render(request, 'knbs_bi/education_csa_primary_schools_by_category_and_subcounty.html', context)

# Add View
def addCategorySubCountyView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/education_csa_primary_schools_by_category_and_subcounty_add.html', context)

# Edit View
def editCategorySubCountyView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/education_csa_primary_schools_by_category_and_subcounty_edit.html', context)


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def primaryCategorySubCounty(request):
    pri_cat = Csa_PrimarySchoolsByCategoryAndSubCounty.objects.all()

    primaries = []

    if pri_cat:
        for primary in pri_cat:
            county = Counties.objects.get(county_id=primary.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=primary.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'county': county.county_name, 'sub_county': sc.subcounty_name, 'schools': primary.no_of_schools,
                         'category': primary.category, 'year': primary.year}
                    primaries.append(c)
    else:
        pass

    return Response(primaries)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addPrimaryCategorySubCounty(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])

    if counties and sub:
        kaunti = counties.county_id
        sub_kaunti = sub.subcounty_id

        primary_add = Csa_PrimarySchoolsByCategoryAndSubCounty(county_id=kaunti, sub_county_id=sub_kaunti,
                                                               no_of_schools=request.data['schools'], category=request.data['category'],
                                                               year=request.data['year'])
        if primary_add:
            primary_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editPrimaryCategorySubCounty(request):
    primary_edit = Csa_PrimarySchoolsByCategoryAndSubCounty.objects.get(primary_schools_id=request.data['primary_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            primary_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            primary_edit.sub_county_id = sub.subcounty_id

    if 'schools' in request.data:
        primary_edit.no_of_schools = request.data['schools']
    if 'category' in request.data:
        primary_edit.category = request.data['category']
    if 'year' in request.data:
        primary_edit.year = request.data['year']

    primary_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

####################################Secondary Enrollment Access Indicators####################################
#launch Page
def secondaryEnrollmentIndicatorsView(request):
    sec_enrol = Csa_SecondaryEnrolmentAndAccessIndicators.objects.all()

    enrollments = []

    if sec_enrol:
        for enrollment in sec_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            c = {'id':enrollment.secondary_enrolment_id, 'county': county.county_name, 'enrollment': enrollment.enrolment, 'gross_enrolment_rate': enrollment.ger,
                 'net_enrollment_rate': enrollment.ner, 'gender': enrollment.gender, 'year': enrollment.year}
            enrollments.append(c)
            context = {'enrollments': enrollments}
    else:
        pass

    return render(request, 'knbs_bi/education_csa_secondary_enrolment_and_access_indicators.html', context)

# Add View
def addSecondaryEnrollmentIndicatorsView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/education_csa_secondary_enrolment_and_access_indicators_add.html', context)

# Edit View
def editSecondaryEnrollmentIndicatorsView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/education_csa_secondary_enrolment_and_access_indicators_edit.html', context)


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def secondaryEnrollmentIndicators(request):
    sec_enrol = Csa_SecondaryEnrolmentAndAccessIndicators.objects.all()

    enrollments = []

    if sec_enrol:
        for enrollment in sec_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            c = {'county': county.county_name, 'enrollment': enrollment.enrolment, 'gross_enrolment_rate': enrollment.ger,
                 'net_enrollment_rate': enrollment.ner, 'gender': enrollment.gender, 'year': enrollment.year}
            enrollments.append(c)
    else:
        pass

    return Response(enrollments)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addSecondaryEnrollmentIndicators(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

    sec_add = Csa_SecondaryEnrolmentAndAccessIndicators(county_id=kaunti, enrolment=request.data['enrollment'],
                                                           ner=request.data['ner'], ger=request.data['ger'], gender=request.data['gender'],
                                                           year=request.data['year'])
    if sec_add:
        sec_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editSecondaryEnrollmentIndicators(request):
    sec_edit = Csa_SecondaryEnrolmentAndAccessIndicators.objects.get(secondary_enrolment_id=request.data['secondary_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            sec_edit.county_id = counties.county_id

    if 'enrollment' in request.data:
        sec_edit.enrolment = request.data['enrollment']
    if 'ner' in request.data:
        sec_edit.ner = request.data['ner']
    if 'ger' in request.data:
        sec_edit.ger = request.data['ger']
    if 'gender' in request.data:
        sec_edit.gender = request.data['gender']
    if 'year' in request.data:
        sec_edit.year = request.data['year']

    sec_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

####################################Teacher Training Colleges####################################
#launch Page
def teacherTrainingCollegesView(request):
    tea_training = Csa_TeacherTrainingColleges.objects.all()

    colleges = []

    if tea_training:
        for college in tea_training:
            county = Counties.objects.get(county_id=college.county_id)
            c = {'id': college.teacher_colleges_id, 'county': county.county_name, 'category': college.category, 'pre_primary': college.pre_primary,
                 'primary': college.primary_sc, 'secondary': college.secondary, 'year': college.year}
            colleges.append(c)
            context = {'colleges': colleges}
    else:
        pass

    return render(request, 'knbs_bi/education_csa_teacher_training_colleges.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def teacherTrainingColleges(request):
    tea_training = Csa_TeacherTrainingColleges.objects.all()

    colleges = []

    if tea_training:
        for college in tea_training:
            county = Counties.objects.get(county_id=college.county_id)
            c = {'county': county.county_name, 'category': college.category, 'pre_primary': college.pre_primary,
                 'primary': college.primary_sc, 'secondary': college.secondary, 'year': college.year}
            colleges.append(c)
    else:
        pass

    return Response(colleges)

# Add View
def addTeacherTrainingCollegesView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/education_csa_teacher_training_colleges_add.html', context)

# Edit View
def editTeacherTrainingCollegesView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/education_csa_teacher_training_colleges_edit.html', context)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addTeacherTrainingColleges(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        tea_training_add = Csa_TeacherTrainingColleges(county_id=kaunti, category=request.data['category'], pre_primary=request.data['pre_primary'], primary_sc=request.data['primary_sc'],
                                                       secondary=request.data['secondary'], year=request.data['year'])
        if tea_training_add:
            tea_training_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editTeacherTrainingColleges(request):
    tea_training_edit = Csa_TeacherTrainingColleges.objects.get(teacher_colleges_id=request.data['college_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            tea_training_edit.county_id = counties.county_id

    if 'category' in request.data:
        tea_training_edit.category = request.data['category']
    if 'pre_primary' in request.data:
        tea_training_edit.pre_primary = request.data['pre_primary']
    if 'primary_sc' in request.data:
        tea_training_edit.primary_sc = request.data['primary_sc']
    if 'secondary' in request.data:
        tea_training_edit.secondary = request.data['secondary']
    if 'year' in request.data:
        tea_training_edit.year = request.data['year']

    tea_training_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

####################################Student Enrollment in Youth in Polytechnics####################################
#Launch Page
def studentEnrollmentPolytechnicView(request):
    stu_enrol = Csa_StudentEnrolmentInYouthPolytechnics.objects.all()

    enrollments = []

    if stu_enrol:
        for enrollment in stu_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=enrollment.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'id': enrollment.youth_poly_id, 'county': county.county_name, 'sub_county': sc.subcounty_name, 'institution_name': enrollment.institution_name,
                         'category': enrollment.category, 'male': enrollment.male, 'female': enrollment.female, 'year': enrollment.year}
                    enrollments.append(c)
                    context = {'enrollments': enrollments}
    else:
        pass

    return render(request, 'knbs_bi/education_csa_student_enrolment_in_youth_polytechnics.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def studentEnrollmentPolytechnic(request):
    stu_enrol = Csa_StudentEnrolmentInYouthPolytechnics.objects.all()

    enrollments = []

    if stu_enrol:
        for enrollment in stu_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=enrollment.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'county': county.county_name, 'sub_county': sc.subcounty_name, 'institution_name': enrollment.institution_name,
                         'category': enrollment.category, 'male': enrollment.male, 'female': enrollment.female, 'year': enrollment.year}
                    enrollments.append(c)
    else:
        pass

    return Response(enrollments)

# Add View
def addStudentEnrollmentPolytechnicView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/education_csa_student_enrolment_in_youth_polytechnics_add.html', context)

# Edit View
def editStudentEnrollmentPolytechnicView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/education_csa_student_enrolment_in_youth_polytechnics_edit.html', context)


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addStudentEnrollmentPolytechnic(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])

    if counties and sub:
        kaunti = counties.county_id
        sub_kaunti = sub.subcounty_id

        stu_enrol_add = Csa_StudentEnrolmentInYouthPolytechnics(county_id=kaunti, sub_county_id=sub_kaunti, institution_name=request.data['institution'],
                                                               category=request.data['category'], male=request.data['male'], female=request.data['female'],
                                                               year=request.data['year'])
        if stu_enrol_add:
            stu_enrol_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editStudentEnrollmentPolytechnic(request):
    stu_enrol_edit = Csa_StudentEnrolmentInYouthPolytechnics.objects.get(youth_poly_id=request.data['poly_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            stu_enrol_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            stu_enrol_edit.sub_county_id = sub.subcounty_id

    if 'institution' in request.data:
        stu_enrol_edit.institution_name = request.data['institution']
    if 'category' in request.data:
        stu_enrol_edit.category = request.data['category']
    if 'male' in request.data:
        stu_enrol_edit.male = request.data['male']
    if 'female' in request.data:
        stu_enrol_edit.female = request.data['female']
    if 'year' in request.data:
        stu_enrol_edit.year = request.data['year']

    stu_enrol_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

####################################ECDE Centres by Category and Subcounty####################################
#Launch Page
def ecdeCategorySubCountyView(request):
    ecde = Csa_EcdeCentresByCategoryAndSubCounty.objects.all()

    centres = []

    if ecde:
        for centre in ecde:
            county = Counties.objects.get(county_id=centre.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=centre.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'id': centre.ecde_centre_id, 'county': county.county_name, 'sub_county': sc.subcounty_name, 'no_of_centres': centre.no_of_centres,
                         'category': centre.category, 'year': centre.year}
                    centres.append(c)
                    context = {'centres': centres}
    else:
        pass

    return render(request, 'knbs_bi/education_csa_ecde_centres_by_category_and_subcounty.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def ecdeCategorySubCounty(request):
    ecde = Csa_EcdeCentresByCategoryAndSubCounty.objects.all()

    centres = []

    if ecde:
        for centre in ecde:
            county = Counties.objects.get(county_id=centre.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=centre.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'county': county.county_name, 'sub_county': sc.subcounty_name, 'no_of_centres': centre.no_of_centres,
                         'category': centre.category, 'year': centre.year}
                    centres.append(c)
    else:
        pass

    return Response(centres)

# Add View
def addEcdeCategorySubCountyView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/education_csa_ecde_centres_by_category_and_subcounty_add.html', context)

# Edit View
def editEcdeCategorySubCountyView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/education_csa_ecde_centres_by_category_and_subcounty_edit.html', context)


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addEcdeCategorySubCounty(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])

    if counties and sub:
        kaunti = counties.county_id
        sub_kaunti = sub.subcounty_id

        ecde_add = Csa_EcdeCentresByCategoryAndSubCounty(county_id=kaunti, sub_county_id=sub_kaunti, no_of_centres=request.data['centres'],
                                                               category=request.data['category'], year=request.data['year'])
        if ecde_add:
            ecde_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editEcdeCategorySubCounty(request):
    ecde_edit = Csa_EcdeCentresByCategoryAndSubCounty.objects.get(ecde_centre_id=request.data['centre_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            ecde_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            ecde_edit.sub_county_id = sub.subcounty_id

    if 'centres' in request.data:
        ecde_edit.no_of_centres = request.data['centres']
    if 'category' in request.data:
        ecde_edit.category = request.data['category']
    if 'year' in request.data:
        ecde_edit.year = request.data['year']

    ecde_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

####################################Primary Enrollment and Access Indicators####################################
#Launch Page
def primaryEnrollmentIndicatorsView(request):
    pri_enrol = Csa_PrimaryEnrolmentAndAccessIndicators.objects.all()

    enrollments = []

    if pri_enrol:
        for enrollment in pri_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            c = {'id': enrollment.primary_enrolment_id, 'county': county.county_name, 'enrollment': enrollment.enrolment, 'gross_enrolment_rate': enrollment.ger,
                 'net_enrollment_rate': enrollment.ner, 'gender': enrollment.gender, 'year': enrollment.year}
            enrollments.append(c)
            context = {'enrollments': enrollments}
    else:
        pass

    return render(request, 'knbs_bi/education_csa_primary_enrolment_and_access_indicators.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def primaryEnrollmentIndicators(request):
    pri_enrol = Csa_PrimaryEnrolmentAndAccessIndicators.objects.all()

    enrollments = []

    if pri_enrol:
        for enrollment in pri_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            c = {'county': county.county_name, 'enrollment': enrollment.enrolment, 'gross_enrolment_rate': enrollment.ger,
                 'net_enrollment_rate': enrollment.ner, 'gender': enrollment.gender, 'year': enrollment.year}
            enrollments.append(c)
    else:
        pass

    return Response(enrollments)

# Add View
def addPrimaryEnrollmentIndicatorsView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/education_csa_primary_enrolment_and_access_indicators_add.html', context)

# Edit View
def editPrimaryEnrollmentIndicatorsView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/education_csa_primary_enrolment_and_access_indicators_edit.html', context)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addPrimaryEnrollmentIndicators(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        enrollment_add = Csa_PrimaryEnrolmentAndAccessIndicators(county_id=kaunti, enrolment=request.data['enrolment'],
                                                               ger=request.data['ger'], ner=request.data['ner'], gender=request.data['gender'],
                                                                 year=request.data['year'])
        if enrollment_add:
            enrollment_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editPrimaryEnrollmentIndicators(request):
    enrolment_edit = Csa_PrimaryEnrolmentAndAccessIndicators.objects.get(primary_enrolment_id=request.data['primary_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            enrolment_edit.county_id = counties.county_id
    if 'enrolment' in request.data:
        enrolment_edit.enrolment = request.data['enrolment']
    if 'ger' in request.data:
        enrolment_edit.ger = request.data['ger']
    if 'ner' in request.data:
        enrolment_edit.ner = request.data['ner']
    if 'gender' in request.data:
        enrolment_edit.gender = request.data['gender']
    if 'year' in request.data:
        enrolment_edit.year = request.data['year']

    enrolment_edit.save()
    return Response(status=status.HTTP_201_CREATED)


####################################Adult Education Centres by Subcounty####################################
#Launch Page
def adultEducationCentresView(request):
    ed_centres = Csa_AdultEducationCentresBySubCounty.objects.all()

    centres = []

    if ed_centres:
        for center in ed_centres:
            county = Counties.objects.get(county_id=center.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=center.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'id': center.adult_centre_id, 'county': county.county_name, 'sub_county': sc.subcounty_name, 'no_centres': center.centres,
                         'year': center.year}
                    centres.append(c)
                    context = {'centres': centres}
    else:
        pass

    return render(request, 'knbs_bi/education_csa_adult_education_centres_by_subcounty.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def adultEducationCentres(request):
    ed_centres = Csa_AdultEducationCentresBySubCounty.objects.all()

    centres = []

    if ed_centres:
        for center in ed_centres:
            county = Counties.objects.get(county_id=center.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=center.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'county': county.county_name, 'sub_county': sc.subcounty_name, 'no_centres': center.centres,
                         'year': center.year}
                    centres.append(c)
    else:
        pass

    return Response(centres)

# Add View
def addAdultEducationCentresView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/education_csa_adult_education_centres_by_subcounty_add.html', context)

# Edit View
def editAdultEducationCentresView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/education_csa_adult_education_centres_by_subcounty_edit.html', context)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAdultEducationCentres(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])

    if counties and sub:
        kaunti = counties.county_id
        sub_kaunti = sub.subcounty_id

        centre_add = Csa_AdultEducationCentresBySubCounty(county_id=kaunti, sub_county_id=sub_kaunti, centres=request.data['centres'],
                                                               year=request.data['year'])
        if centre_add:
            centre_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAdultEducationCentres(request):
    centre_edit = Csa_AdultEducationCentresBySubCounty.objects.get(adult_centre_id=request.data['centre_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            centre_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            centre_edit.sub_county_id = sub.subcounty_id

    if 'centres' in request.data:
        centre_edit.centres = request.data['centres']
    if 'year' in request.data:
        centre_edit.year = request.data['year']

    centre_edit.save()
    return Response(status=status.HTTP_201_CREATED)

####################################Adult Education Enrollment by Sex and Subcounty####################################
#Launch Page
def adultEducationEnrolmentView(request):
    ed_enrol = Csa_AdultEducationEnrolmentBySexAndSubcounty.objects.all()

    enrollments = []

    if ed_enrol:
        for enrollment in ed_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=enrollment.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'id': enrollment.adult_enrolment_id, 'county': county.county_name, 'sub_county': sc.subcounty_name, 'number': enrollment.number,
                         'gender': enrollment.gender, 'year': enrollment.year}
                    enrollments.append(c)
                    context = {'enrollments': enrollments}

    else:
        pass

    return render(request, 'knbs_bi/education_csa_adult_education_enrolment_by_sex_and_subcounty.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def adultEducationEnrolment(request):
    ed_enrol = Csa_AdultEducationEnrolmentBySexAndSubcounty.objects.all()

    enrollments = []

    if ed_enrol:
        for enrollment in ed_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=enrollment.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'county': county.county_name, 'sub_county': sc.subcounty_name, 'number': enrollment.number,
                         'gender': enrollment.gender, 'year': enrollment.year}
                    enrollments.append(c)

    else:
        pass

    return Response(enrollments)

# Add View
def addAdultEducationEnrolmentView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/education_csa_adult_education_enrolment_by_sex_and_subcounty_add.html', context)

# Edit View
def editAdultEducationEnrolmentView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/education_csa_adult_education_enrolment_by_sex_and_subcounty_edit.html', context)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAdultEducationEnrolment(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])

    if counties and sub:
        kaunti = counties.county_id
        sub_kaunti = sub.subcounty_id

        enrollment_add = Csa_AdultEducationEnrolmentBySexAndSubcounty(county_id=kaunti, sub_county_id=sub_kaunti, number=request.data['number'],
                                                                  gender=request.data['gender'], year=request.data['year'])
        if enrollment_add:
            enrollment_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAdultEducationEnrolment(request):
    enrollment_edit = Csa_AdultEducationEnrolmentBySexAndSubcounty.objects.get(adult_enrolment_id=request.data['enrolment_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            enrollment_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            enrollment_edit.sub_county_id = sub.subcounty_id

    if 'number' in request.data:
        enrollment_edit.number = request.data['number']
    if 'gender' in request.data:
        enrollment_edit.gender = request.data['gender']
    if 'year' in request.data:
        enrollment_edit.year = request.data['year']

    enrollment_edit.save()
    return Response(status=status.HTTP_201_CREATED)

####################################Adult Education Proficiency Test Results####################################
#Launch Page
def adultEducationProficiencyView(request):
    ed_proficiency = Csa_AdultEducationProficiencyTestResults.objects.all()

    proficiencies = []

    if ed_proficiency:
        for proficiency in ed_proficiency:
            county = Counties.objects.get(county_id=proficiency.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=proficiency.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'id': proficiency.adult_proficiency_id, 'county': county.county_name, 'sub_county': sc.subcounty_name, 'no_sat': proficiency.no_sat,
                         'no_passed': proficiency.no_passed, 'gender': proficiency.gender, 'year': proficiency.year}
                    proficiencies.append(c)
                    context = {'proficiencies': proficiencies}
    else:
        pass

    return render(request, 'knbs_bi/education_csa_adult_education_proficiency_test_results.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def adultEducationProficiency(request):
    ed_proficiency = Csa_AdultEducationProficiencyTestResults.objects.all()

    proficiencies = []

    if ed_proficiency:
        for proficiency in ed_proficiency:
            county = Counties.objects.get(county_id=proficiency.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=proficiency.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'county': county.county_name, 'sub_county': sc.subcounty_name, 'no_sat': proficiency.no_sat,
                         'no_passed': proficiency.no_passed, 'gender': proficiency.gender, 'year': proficiency.year}
                    proficiencies.append(c)
    else:
        pass

    return Response(proficiencies)

# Add View
def addAdultEducationProficiencyView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/education_csa_adult_education_proficiency_test_results_add.html', context)

# Edit View
def editAdultEducationProficiencyView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/education_csa_adult_education_proficiency_test_results_edit.html', context)


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAdultEducationProficiency(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])

    if counties and sub:
        kaunti = counties.county_id
        sub_kaunti = sub.subcounty_id

        ed_proficiency_add = Csa_AdultEducationProficiencyTestResults(county_id=kaunti, sub_county_id=sub_kaunti, no_sat=request.data['sat'],
                                                               no_passed=request.data['passed'], gender=request.data['gender'], year=request.data['year'])
        if ed_proficiency_add:
            ed_proficiency_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAdultEducationProficiency(request):
    ed_proficiency_edit = Csa_AdultEducationProficiencyTestResults.objects.get(adult_proficiency_id=request.data['adult_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            ed_proficiency_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            ed_proficiency_edit.sub_county_id = sub.subcounty_id

    if 'sat' in request.data:
        ed_proficiency_edit.no_sat = request.data['sat']
    if 'passed' in request.data:
        ed_proficiency_edit.no_passed = request.data['passed']
    if 'gender' in request.data:
        ed_proficiency_edit.gender = request.data['gender']
    if 'year' in request.data:
        ed_proficiency_edit.year = request.data['year']

    ed_proficiency_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


############################################Edstat############################################
####################################Edstat_Ecde_Enrollment_And_Enrollment_Rates_By_County####################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def ecdeEnrollmentEdstat(request):
    ecde_enrol = Edstat_Ecde_Enrollment_And_Enrollment_Rates_By_County.objects.all()

    enrollments = []

    if ecde_enrol:
        for enrollment in ecde_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            c = {'county': county.county_name, 'enrollment': enrollment.ecde_enrollment, 'ger': enrollment.gross_enrollment_rate,
                 'ner': enrollment.net_enrollment_rate, 'gender': enrollment.gender, 'year': enrollment.year}
            enrollments.append(c)
    else:
        pass
    return Response(enrollments)

#Launch Page
def ecdeEnrollmentView(request):
    ecde_enrol = Edstat_Ecde_Enrollment_And_Enrollment_Rates_By_County.objects.all()

    enrollments = []

    if ecde_enrol:
        for enrollment in ecde_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            c = {'id': enrollment.ecde_enrollment_id, 'county': county.county_name, 'enrollment': enrollment.ecde_enrollment, 'ger': enrollment.gross_enrollment_rate,
                 'ner': enrollment.net_enrollment_rate, 'gender': enrollment.gender, 'year': enrollment.year}
            enrollments.append(c)
            context = {'enrollments': enrollments}
    return render(request, 'knbs_bi/education_edstat_ecde_enrollment_and_enrollment_rates_by_county.html', context)

#Ecde Enrollment Add View
def addEcdeEnrollmentView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    # translation.activate('en')
    return render(request, 'knbs_bi/education_edstat_ecde_enrollment_and_enrollment_rates_by_county_add.html', context)

#Ecde Enrollment Edit View
def editEcdeEnrollmentView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/education_edstat_ecde_enrollment_and_enrollment_rates_by_county_edit.html', context)

#Add School Enrollment
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addEcdeEnrollment(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        ecde_add = Edstat_Ecde_Enrollment_And_Enrollment_Rates_By_County(county_id=kaunti, ecde_enrollment=request.data['enrollment'],
                                                                         gross_enrollment_rate=request.data['ger'], net_enrollment_rate=request.data['ner'],
                                                                         gender=request.data['gender'], year=request.data['year'])
        if ecde_add:
            ecde_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit School Enrollment
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editEcdeEnrollment(request):
    ecde_edit = Edstat_Ecde_Enrollment_And_Enrollment_Rates_By_County.objects.get(ecde_enrollment_id=request.data['enrollment_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            ecde_edit.county_id = counties.county_id
    if 'enrollment' in request.data:
        ecde_edit.ecde_enrollment = request.data['enrollment']
    if 'ger' in request.data:
        ecde_edit.gross_enrollment_rate = request.data['ger']
    if 'ner' in request.data:
        ecde_edit.net_enrollment_rate = request.data['ner']
    if 'gender' in request.data:
        ecde_edit.gender = request.data['gender']
    if 'year' in request.data:
        ecde_edit.year = request.data['year']

    ecde_edit.save()
    return Response(status=status.HTTP_201_CREATED)


####################################Edstat_Primary_Enrollment_Enrollment_Rates_County####################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def primaryEnrollmentEdstat(request):
    primary_enrol = Edstat_Primary_Enrollment_Enrollment_Rates_County.objects.all()

    enrollments = []

    if primary_enrol:
        for enrollment in primary_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            c = {'county': county.county_name, 'enrollment': enrollment.primary_enrollment, 'ger': enrollment.gross_enrollment_rate,
                 'ner': enrollment.net_enrollment_rate, 'gender': enrollment.gender, 'year': enrollment.year}
            enrollments.append(c)
    else:
        pass
    return Response(enrollments)

#Launch Page
def primaryEnrollmentView(request):
    primary_enrol = Edstat_Primary_Enrollment_Enrollment_Rates_County.objects.all()

    enrollments = []

    if primary_enrol:
        for enrollment in primary_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            c = {'id': enrollment.primary_enrollment_id,'county': county.county_name, 'enrollment': enrollment.primary_enrollment,
                 'ger': enrollment.gross_enrollment_rate, 'ner': enrollment.net_enrollment_rate, 'gender': enrollment.gender,
                 'year': enrollment.year}
            enrollments.append(c)
            context = {'enrollments': enrollments}
    return render(request, 'knbs_bi/education_edstat_primary_enrollment_and_enrollment_rates_by_county.html', context)

#Primary Enrollment Add View
def addPrimaryEnrollmentView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    # translation.activate('en')
    return render(request, 'knbs_bi/education_edstat_primary_enrollment_and_enrollment_rates_by_county_add.html', context)

#Primary Enrollment Edit View
def editPrimaryEnrollmentView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/education_edstat_primary_enrollment_and_enrollment_rates_by_county_edit.html', context)

#Add School Enrollment
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addPrimaryEnrollment(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        pri_add = Edstat_Primary_Enrollment_Enrollment_Rates_County(county_id=kaunti, primary_enrollment=request.data['enrollment'],
                                                                         gross_enrollment_rate=request.data['ger'], net_enrollment_rate=request.data['ner'],
                                                                         gender=request.data['gender'], year=request.data['year'])
        if pri_add:
            pri_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit School Enrollment
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editPrimarynrollment(request):
    pri_edit = Edstat_Primary_Enrollment_Enrollment_Rates_County.objects.get(primary_enrollment_id=request.data['enrollment_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            pri_edit.county_id = counties.county_id
    if 'enrollment' in request.data:
        pri_edit.primary_enrollment = request.data['enrollment']
    if 'ger' in request.data:
        pri_edit.gross_enrollment_rate = request.data['ger']
    if 'ner' in request.data:
        pri_edit.net_enrollment_rate = request.data['ner']
    if 'gender' in request.data:
        pri_edit.gender = request.data['gender']
    if 'year' in request.data:
        pri_edit.year = request.data['year']

    pri_edit.save()
    return Response(status=status.HTTP_201_CREATED)

####################################Edstat_Secondary_Enrollment_Enrollment_Rates_County####################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def secondaryEnrollmentEdstat(request):
    secondary_enrol = Edstat_Secondary_Enrollment_Enrollment_Rates_County.objects.all()

    enrollments = []

    if secondary_enrol:
        for enrollment in secondary_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            c = {'county': county.county_name, 'enrollment': enrollment.secondary_enrollment, 'ger': enrollment.gross_enrollment_rate,
                 'ner': enrollment.net_enrollment_rate, 'gender': enrollment.gender, 'year': enrollment.year}
            enrollments.append(c)
    else:
        pass
    return Response(enrollments)

#Launch Page
def secondaryEnrollmentView(request):
    secondary_enrol = Edstat_Secondary_Enrollment_Enrollment_Rates_County.objects.all()

    enrollments = []

    if secondary_enrol:
        for enrollment in secondary_enrol:
            county = Counties.objects.get(county_id=enrollment.county_id)
            c = {'id': enrollment.secondary_enrollment_id,'county': county.county_name, 'enrollment': enrollment.secondary_enrollment,
                 'ger': enrollment.gross_enrollment_rate, 'ner': enrollment.net_enrollment_rate, 'gender': enrollment.gender,
                 'year': enrollment.year}
            enrollments.append(c)
            context = {'enrollments': enrollments}
    return render(request, 'knbs_bi/education_edstat_secondary_enrollment_and_enrollment_rates_by_county.html', context)

#Secondary Enrollment Add View
def addSecondaryEnrollmentView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    # translation.activate('en')
    return render(request, 'knbs_bi/education_edstat_secondary_enrollment_and_enrollment_rates_by_county_add.html', context)

#Secondary Enrollment Edit View
def editSecondaryEnrollmentView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/education_edstat_secondary_enrollment_and_enrollment_rates_by_county_edit.html', context)

#Add School Enrollment
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addSecondaryEnrollment(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        sec_add = Edstat_Secondary_Enrollment_Enrollment_Rates_County(county_id=kaunti, secondary_enrollment=request.data['enrollment'],
                                                                         gross_enrollment_rate=request.data['ger'], net_enrollment_rate=request.data['ner'],
                                                                         gender=request.data['gender'], year=request.data['year'])
        if sec_add:
            sec_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit School Enrollment
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editSecondarynrollment(request):
    sec_edit = Edstat_Secondary_Enrollment_Enrollment_Rates_County.objects.get(secondary_enrollment_id=request.data['enrollment_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            sec_edit.county_id = counties.county_id
    if 'enrollment' in request.data:
        sec_edit.secondary_enrollment = request.data['enrollment']
    if 'ger' in request.data:
        sec_edit.gross_enrollment_rate = request.data['ger']
    if 'ner' in request.data:
        sec_edit.net_enrollment_rate = request.data['ner']
    if 'gender' in request.data:
        sec_edit.gender = request.data['gender']
    if 'year' in request.data:
        sec_edit.year = request.data['year']

    sec_edit.save()
    return Response(status=status.HTTP_201_CREATED)

####################################Edstat_Kcpe_Examination_Candidature####################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def kcpeCandidature(request):
    kcpe = Edstat_Kcpe_Examination_Candidature.objects.all()

    candidatures = []

    if kcpe:
        for candidature in kcpe:
            c = {'candidature': candidature.kcpe_candidature, 'gender': candidature.gender, 'year': candidature.year}
            candidatures.append(c)
    else:
        pass
    return Response(candidatures)

#Launch Page
def kcpeCandidatureView(request):
    kcpe = Edstat_Kcpe_Examination_Candidature.objects.all()

    candidatures = []

    if kcpe:
        for candidature in kcpe:
            c = {'id': candidature.candidature_id, 'candidature': candidature.kcpe_candidature, 'gender': candidature.gender,
                 'year': candidature.year}
            candidatures.append(c)
            context = {'candidatures': candidatures}
    return render(request, 'knbs_bi/education_edstat_kcpe_examination_candidature.html', context)

#Kcpe Examination Add View
def addKcpeCandidatureView(request):
    return render(request, 'knbs_bi/education_edstat_kcpe_examination_candidature_add.html')

#Kcpe Examination Edit View
def editKcpeCandidatureView(request):
    return render(request, 'knbs_bi/education_edstat_kcpe_examination_candidature_edit.html')

#Add School Enrollment
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addKcpeCandidature(request):
    kcpe_add = Edstat_Kcpe_Examination_Candidature(kcpe_candidature=request.data['candidature'],gender=request.data['gender'],
                                                   year=request.data['year'])
    if kcpe_add:
        kcpe_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit School Enrollment
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editKcpeCandidature(request):
    kcpe_edit = Edstat_Kcpe_Examination_Candidature.objects.get(candidature_id=request.data['candidature_id'])

    if 'candidature' in request.data:
        kcpe_edit.kcpe_candidature = request.data['candidature']
    if 'gender' in request.data:
        kcpe_edit.gender = request.data['gender']
    if 'year' in request.data:
        kcpe_edit.year = request.data['year']

    kcpe_edit.save()
    return Response(status=status.HTTP_201_CREATED)

####################################Edstat_Kcpe_Examination_Results_By_Subject####################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def kcpeResults(request):
    kcpe = Edstat_Kcpe_Examination_Results_By_Subject.objects.all()

    results = []

    if kcpe:
        for result in kcpe:
            c = {'result': result.kcpe_result, 'subject': result.subject, 'year': result.year}
            results.append(c)
    else:
        pass
    return Response(results)

#Launch Page
def kcpeResultsView(request):
    kcpe = Edstat_Kcpe_Examination_Results_By_Subject.objects.all()

    results = []

    if kcpe:
        for result in kcpe:
            c = {'id': result.kcpe_result_id, 'result': result.kcpe_result, 'subject': result.subject, 'year': result.year}
            results.append(c)
            context = {'results': results}
    return render(request, 'knbs_bi/education_edstat_kcpe_examination_results_by_subject.html', context)

#Kcpe Results Add View
def addKcpeResultsView(request):
    return render(request, 'knbs_bi/education_edstat_kcpe_examination_results_by_subject_add.html')

#Kcpe Results Edit View
def editKcpeResultsView(request):
    return render(request, 'knbs_bi/education_edstat_kcpe_examination_results_by_subject_edit.html')

#Add School Enrollment
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addKcpeResults(request):
    kcpe_add = Edstat_Kcpe_Examination_Results_By_Subject(kcpe_result=request.data['result'],subject=request.data['subject'],
                                                   year=request.data['year'])
    if kcpe_add:
        kcpe_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit School Enrollment
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editKcpeResults(request):
    kcpe_edit = Edstat_Kcpe_Examination_Results_By_Subject.objects.get(kcpe_result_id=request.data['result_id'])

    if 'result' in request.data:
        kcpe_edit.kcpe_result = request.data['result']
    if 'subject' in request.data:
        kcpe_edit.subject = request.data['subject']
    if 'year' in request.data:
        kcpe_edit.year = request.data['year']

    kcpe_edit.save()
    return Response(status=status.HTTP_201_CREATED)


####################################Edstat_Kcse_Examination_Results####################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def kcseResults(request):
    kcse = Edstat_Kcse_Examination_Results.objects.all()

    results = []

    if kcse:
        for result in kcse:
            c = {'candidates': result.number_of_candidates, 'grade': result.kcse_grade, 'sex': result.sex, 'year': result.year}
            results.append(c)
    else:
        pass
    return Response(results)

#Launch Page
def kcseResults(request):
    kcse = Edstat_Kcse_Examination_Results.objects.all()

    results = []

    if kcse:
        for result in kcse:
            c = {'id': result.kcse_result_id, 'candidates': result.number_of_candidates, 'grade': result.kcse_grade, 'sex': result.sex,
                 'year': result.year}
            results.append(c)
            context = {'results': results}
    return render(request, 'knbs_bi/education_edstat_kcse_examination_results.html', context)

#Kcse Results Add View
def addKcseResultsView(request):
    return render(request, 'knbs_bi/education_edstat_kcse_examination_results_add.html')

#Kcse Results Edit View
def editKcseResultsView(request):
    return render(request, 'knbs_bi/education_edstat_kcse_examination_results_edit.html')

#Add School Enrollment
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addKcseResults(request):
    kcse_add = Edstat_Kcse_Examination_Results(number_of_candidates=request.data['candidates'], kcse_grade=request.data['grade'],
                                               sex=request.data['sex'], year=request.data['year'])
    if kcse_add:
        kcse_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit School Enrollment
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editKcseResults(request):
    kcse_edit = Edstat_Kcse_Examination_Results.objects.get(kcse_result_id=request.data['result_id'])

    if 'candidates' in request.data:
        kcse_edit.number_of_candidates = request.data['candidates']
    if 'grade' in request.data:
        kcse_edit.kcse_grade = request.data['grade']
    if 'sex' in request.data:
        kcse_edit.sex = request.data['sex']
    if 'year' in request.data:
        kcse_edit.year = request.data['year']

    kcse_edit.save()
    return Response(status=status.HTTP_201_CREATED)

