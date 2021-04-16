from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

# ...all baseball leagues
# ...all womens' leagues
# ...all leagues where sport is any type of hockey
# ...all leagues where sport is something OTHER THAN football
# ...all leagues that call themselves "conferences"
# ...all leagues in the Atlantic region
# ...all teams based in Dallas
# ...all teams named the Raptors
# ...all teams whose location includes "City"
# ...all teams whose names begin with "T"
# ...all teams, ordered alphabetically by location
# ...all teams, ordered by team name in reverse alphabetical order
# ...every player with last name "Cooper"
# ...every player with first name "Joshua"
# ...every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
# ...all players with first name "Alexander" OR first name "Wyatt"

def index(request):
	context = {
		"baseball_leagues": League.objects.filter(name__contains='baseball'),
		"women_leagues": League.objects.filter(name__contains='women'),
		"hockey_leagues": League.objects.filter(sport__contains='hockey'),
		"non_football_leagues": League.objects.exclude(sport__contains='football'),
		"conference_leagues": League.objects.filter(name__contains='conference'),
		"atlantic_leagues": League.objects.filter(name__contains='atlantic'),
		"dallas_teams": Team.objects.filter(location__contains="dallas"),
		"raptors_teams": Team.objects.filter(team_name__contains="raptors"),
		"city_teams": Team.objects.filter(location__contains="city"),
		"start_t_teams": Team.objects.filter(team_name__startswith="t"),
		"orderby_location_teams": Team.objects.all().order_by('location'),
		"reverse_name_teams": Team.objects.all().order_by('-team_name'),
		"cooper_last_players": Player.objects.filter(last_name__contains="cooper"),
		"joshua_first_players": Player.objects.filter(first_name__contains="joshua"),
		"cooper_last_non_joshua_first_players": Player.objects.filter(last_name__contains="cooper").exclude(first_name__contains="joshua"),
		"alexander_or_wyatt_first_players": Player.objects.filter(first_name__contains="alexander") | Player.objects.filter(first_name__contains="wyatt"),
	}
	return render(request, "leagues/index.html", context)

# ...all teams in the Atlantic Soccer Conference
# ...all (current) players on the Boston Penguins
# ...all (current) players in the International Collegiate Baseball Conference
# ...all (current) players in the American Conference of Amateur Football with last name "Lopez"
# ...all football players
# ...all teams with a (current) player named "Sophia"
# ...all leagues with a (current) player named "Sophia"
# ...everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders
# ...all teams, past and present, that Samuel Evans has played with
# ...all players, past and present, with the Manitoba Tiger-Cats
# ...all players who were formerly (but aren't currently) with the Wichita Vikings
# ...every team that Jacob Gray played for before he joined the Oregon Colts
# ...everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
# ...all teams that have had 12 or more players, past and present. (HINT: Look up the Django annotate function.)
# ...all players and count of teams played for, sorted by the number of teams they've played for

def index_2(request):
	context = {
		"atlantic_soccer_league_teams": Team.objects.filter(league__name__contains='atlantic').filter(league__sport__contains='soccer'),
		"boston_penguins_players": Player.objects.filter(curr_team__location__contains='boston').filter(curr_team__team_name__contains='penguins'),
		"international_collegiate_baseball_conference_teams": Team.objects.filter(league__name__contains='International Collegiate Baseball Conference'),
		"american_conference_amateur_football_lopez_last_players": Player.objects.filter(last_name__contains='Lopez').filter(curr_team__league__name__contains='American Conference of Amateur Football'),
		"football_players": Player.objects.filter(curr_team__league__sport__contains='football'),
		"sophia_first_player_teams": Team.objects.filter(curr_players__first_name__contains='sophia'),
		"sophia_first_player_leagues": League.objects.filter(teams__curr_players__first_name__contains='sophia'),
		"flores_last_notplay_washington_roughriders_players": Player.objects.filter(last_name__contains='Flores').exclude(curr_team__location__contains='washington').exclude(curr_team__team_name__contains='roughriders'),
		"samuel_evans_allteams": Team.objects.filter(all_players__first_name__contains='samuel').filter(all_players__last_name__contains='evans'),
		"manitoba_tigercats_allplayers": Player.objects.filter(all_teams__location__contains='manitoba').filter(all_teams__team_name__contains='tiger-cats'),
		"wichita_vikings_formerplayers": Player.objects.filter(all_teams__location__contains='wichita').filter(all_teams__team_name__contains='vikings').exclude(curr_team__location__contains='wichita').exclude(curr_team__team_name__contains='vikings'),
		# "jacob_gary_before_oregon_colts_teams" is not sure
		"jacob_gary_before_oregon_colts_teams": Team.objects.filter(all_players__first_name__contains='jacob').filter(all_players__last_name__contains='gray').filter(id__lt=24),
		"joshua_first_atlantic_federation_of_amateur_baseball_players": Player.objects.filter(first_name__contains='joshua').filter(all_teams__league__name__contains='atlantic federation of amateur baseball'),
		"12_more_players_alltime_teams": Team.objects.annotate(Count('all_players')).filter(all_players__count__gte=12),
		"count_of_teams_played_all_players": Player.objects.annotate(num_played_for=Count('all_teams')).order_by('-num_played_for'),
	}
	return render(request, "leagues/index2.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")