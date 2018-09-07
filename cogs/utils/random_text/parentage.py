from random import choice
from cogs.utils.custom_bot import CustomBot


class ParentageRandomText(object):

    def __init__(self, bot:CustomBot):
        self.bot = bot

    @staticmethod
    def valid_parent_choice(instigator, target):
        '''
        When the instigator asks the target to be their parent
        '''

        return choice([
            f"{instigator.mention} wants to adopt you, {target.mention}. Do you accept?",
            f"{instigator.mention} wants to share the love and make you their child, {target.mention}. What do you think?",
            f"{instigator.mention} would love to adopt you, {target.mention}. What do you think?",
            f"{target.mention}, today's your lucky day. {instigator.mention} wants to adopt you. Do you accept?",
            f"{target.mention}, {instigator.mention} wants to be your parent. What do you say?",
            f"{target.mention}, do you want to be {instigator.mention}'s parent?",
        ])


    @staticmethod
    def parent_is_family(instigator, target):
        '''
        When the instigator picks the target as a parent but they're already family members
        '''

        return choice([
            f"They're already part of the family you're in, {instigator.mention}.",
            f"You can't just mess up your family tree like that - you're already related to that person, {instigator.mention}.",
            f"Family trees tend to get messed up when you get relations like that, so I'm gonna have to say no, {instigator.mention}.",
            f"{instigator.mention}, they're already part of your family.",
        ])


    @staticmethod
    def parent_is_me(instigator, target):
        '''
        The instigator picked the bot as a parent
        '''

        return choice([
            "I'm afraid I'll have to decline, but thank you for the offer.",
            "Not that I don't _like_ you or anything, but I would rather not.",
            "You can't adopt any robots, me included. Sorry!",
            "Though I'd love to, I can't.",
            "I'm sure I'd be a wonderful child, but I can't set you as my child.",
            "Thanks for the offer, but no thank you.",
        ])


    @staticmethod
    def parent_is_bot(instigator, target):
        '''
        The instigator wants to parentify a bot
        '''

        return choice([
            f"Bots don't make _terribly_ good parents, but I'll allow it, {instigator.mention}. Have fun with your new family!",
            f"Though robots often have trouble with love, I'm sure {target.mention} will make a lovely parent for you, {instigator.mention}.",
            f"Your choice of robot is... interesting. {target.mention} is now your parent, {instigator.mention}!",
            f"A robot probably isn't the best choice, but who am I to judge? Have fun with your new family, {instigator.mention}!",
        ])


    @staticmethod
    def parent_while_instigator(instigator, target):
        '''
        When the instigator asks the target to be their parent while they've already asked another
        '''

        return choice([
            f"Hold your horses, {instigator.mention}, you've already made a proposition to someone.",
            "Slow down a bit - wait for a response to your other question.",
            "Though I hate to rain on your parade, you can only make one proposition at a time.",
            f"Chill. One proposal at a time, {instigator.mention}.",
            "You can only make or recieve one proposition at a time.",
        ])


    @staticmethod
    def parent_to_instigator(instigator, target):
        '''
        When the person you're responding to asked someone out
        '''

        return choice([
            "They've just proposed to someone. Give it a minute.",
            "Give them a minute to deal with their proposal and then try again.",
            "Looks like they're focused on something else right now. Try again in a minute.",
            f"Holdup, {instigator.mention}, they've just proposed to someone else.",
        ])


    @staticmethod
    def parent_while_target(instigator, target):
        '''
        When the instigator has another proposal to respond to
        '''

        return choice([
            f"Shouldn't you respond to your other question first, {instigator.mention}?",
            f"I think you should prioritise your other proposal, {instigator.mention}.",
            f"You've already been asked something, {instigator.mention} - you should deal with that first.",
            "You can only make or recieve one proposition at a time.",
        ])


    @staticmethod
    def parent_to_target(instigator, target):
        '''
        When the target is also someone elses' target
        '''

        return choice([
            "Oops, looks like someone else asked first. Just wait a minute and see what they say.",
            "Someone already made a proposition to them, try again in a minute.",
            "Looks like you'll need to wait until they respond to your current offer.",
            "Unfotrunately they need to respond to their current proposal before you can make yours.",
        ])


    @staticmethod
    def parent_yourself(instigator, target):
        '''
        Picking yourself as your parent
        '''

        return choice([
            "Oh, ha ha, very funny.",
            "I'm not super sure why you thought that would work.",
            "Try picking someone that isn't yourself next time!",
            "Oddly enough, you can't adopt yourself. I wonder why that is?",
            "You can't adopt yourself, I'm sorry to say.",
        ])


    @staticmethod
    def parent_while_adopted(instigator, target):
        '''
        Picking a parent while you already have one
        '''

        return choice([
            f"I know it's a strange setup, but you can only pick one of your parents, {instigator.mention}.",
            f"You have a parent already, {instigator.mention}.",
            f"You can only have one parent at a time, as odd as that sounds, {instigator.mention}.",
            f"You can't pick a new parent while you already have one, {instigator.mention}.",
        ])


    @staticmethod
    def parent_request_timeout(instigator, target):
        '''
        Parent request timed out
        '''

        return choice([
            f"Sorry, {instigator.mention}, but back to the orphanage with you.",
            f"No response from your decided daddy, {instigator.mention}. Sorry about that.",
            f"No response. Huh. Guess you'll have to remain parentless for now, {instigator.mention}.",
            f"Ouch. No response. Sorry, {instigator.mention}. I'll take you out for ice cream later.",
            f"They didn't seem to say anything, {instigator.mention}. Maybe try again later!",
            f"Sorry to say this, {instigator.mention}, but they didn't get back in time to respond.",
            f"{instigator.mention}, your parent request has timed out. Try again when they're online!",
        ])


    @staticmethod
    def parent_request_accept(instigator, target):
        '''
        Accepted parent request
        '''

        return choice([
            f"{instigator.mention}, meet your new parent, {target.mention}!",
            f"{target.mention}, you have sucessfully adopted {instigator.mention}!",
            f"I'm happy to introduce {instigator.mention} to the {target.mention} family!",
            f"They accepted, {instigator.mention}! Welcome to the new family.",
        ])


    @staticmethod
    def parent_request_deny(instigator, target):
        '''
        When the parent request is denied
        '''

        return choice([
            f"Sorry, {instigator.mention}, but they said no.",
            f"Unfortunately they said no, {instigator.mention}. Better luck next time!",
            f"It seems they aren't ready to be your parent, {instigator.mention}.",
            f"{instigator.mention}, your new parent is {target.mention} c:",
        ])


def setup(bot:CustomBot):
    x = ParentageRandomText(bot)
    bot.add_cog(x)
